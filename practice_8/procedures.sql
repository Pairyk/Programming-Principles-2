CREATE OR REPLACE PROCEDURE upsert_contact(p_name TEXT, p_phone TEXT)
LANGUAGE plpgsql AS $$
BEGIN
    -- We check 'user_name' because that is your column name
    IF EXISTS (SELECT 1 FROM public.contacts WHERE user_name = p_name) THEN
        UPDATE public.contacts 
        SET phone_number = p_phone 
        WHERE user_name = p_name;
    ELSE
        -- We insert into 'user_name' and 'phone_number'
        INSERT INTO public.contacts(user_name, phone_number) 
        VALUES(p_name, p_phone);
    END IF;
END;
$$;

--- 3. THE DELETE PROCEDURE
CREATE OR REPLACE PROCEDURE delete_contact(p_search TEXT)
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM public.contacts 
    WHERE user_name = p_search OR phone_number = p_search;
END;
$$;

--- 4. THE BULK UPSERT
CREATE OR REPLACE PROCEDURE bulk_upsert_contacts(p_names TEXT[], p_phones TEXT[])
LANGUAGE plpgsql AS $$
DECLARE
    i INT;
BEGIN
    -- Ensure we have data to loop through
    IF p_names IS NOT NULL AND array_length(p_names, 1) > 0 THEN
        FOR i IN array_lower(p_names, 1) .. array_upper(p_names, 1) LOOP
            
            -- Validation: Regex for valid phone characters
            IF p_phones[i] ~ '^[0-9\-\+\(\) ]+$' THEN
                -- Calls the fixed TEXT-based upsert above
                CALL upsert_contact(p_names[i], p_phones[i]);
            ELSE
                RAISE NOTICE 'Skipping invalid phone format for: %', p_names[i];
            END IF;
            
        END LOOP;
    END IF;
END;
$$;