CREATE OR REPLACE FUNCTION search_artifacts(p_pattern TEXT)
RETURNS TABLE(id INT, name TEXT, buff TEXT) AS $$
BEGIN
    RETURN QUERY 
    SELECT a.id, a.name, a.buff 
    FROM artifacts a
    WHERE a.name ILIKE '%' || p_pattern || '%' 
       OR a.buff ILIKE '%' || p_pattern || '%';
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION get_artifacts(p_limit INT, p_offset INT)
RETURNS TABLE(id INT, name TEXT, buff TEXT) AS $$
BEGIN
    RETURN QUERY 
    SELECT a.id, a.name, a.buff 
    FROM artifacts a
    ORDER BY a.id
    LIMIT p_limit 
    OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;