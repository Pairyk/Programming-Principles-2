-- 1. Pattern Search Function
-- Returns a table of results matching a string in name or phone
CREATE OR REPLACE FUNCTION search_contacts(p_pattern TEXT)
RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY 
    SELECT c.id, c.name, c.phone 
    FROM contacts c
    WHERE c.name ILIKE '%' || p_pattern || '%' 
       OR c.phone ILIKE '%' || p_pattern || '%';
END;
$$ LANGUAGE plpgsql;

-- 2. Pagination Function
-- Returns a "page" of data based on a limit and an offset
CREATE OR REPLACE FUNCTION get_contacts_paginated(p_limit INT, p_offset INT)
RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY 
    SELECT c.id, c.name, c.phone 
    FROM contacts c
    ORDER BY c.id
    LIMIT p_limit 
    OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;