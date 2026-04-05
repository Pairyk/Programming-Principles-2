CREATE OR REPLACE PROCEDURE upsert_artifact(p_name TEXT, p_buff TEXT)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM public.artifacts WHERE name = p_name) THEN
        UPDATE public.artifacts 
        SET buff = p_buff 
        WHERE name = p_name;
    ELSE
        INSERT INTO public.artifacts(name, buff) 
        VALUES(p_name, p_buff);
    END IF;
END;
$$;

CREATE OR REPLACE PROCEDURE delete_artifact(p_search TEXT)
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM public.artifacts
    WHERE name = p_search OR buff = p_search;

    IF FOUND THEN
        RAISE NOTICE 'Artifact(s) matching "%" were deleted.', p_search;
    ELSE
        RAISE NOTICE 'No artifacts found matching "%".', p_search;
    END IF;
END;
$$;

CREATE OR REPLACE PROCEDURE bulk_upsert_artifacts(p_names TEXT[], p_buffs TEXT[])
LANGUAGE plpgsql AS $$
DECLARE
    i INT;
BEGIN
    IF p_names IS NOT NULL AND array_length(p_names, 1) > 0 THEN
        FOR i IN array_lower(p_names, 1) .. array_upper(p_names, 1) LOOP
            IF p_names IS NOT NULL AND length(p_buffs[i]) >= 3 THEN 
                CALL upsert_artifact(p_names[i], p_buffs[i]);
            ELSE
                RAISE NOTICE 'Skipping invalid data at index %: %', i, p_names[i];
            END IF;
        END LOOP;
    END IF;
END;
$$;