CREATE OR REPLACE FUNCTION audit_log_trigger() RETURNS TRIGGER AS $$
BEGIN
    IF (TG_OP = 'DELETE') THEN
        INSERT INTO documents_changelog(document_id, old_data, new_data) VALUES (OLD.id, OLD.data, Null);
    ELSIF (TG_OP = 'UPDATE') THEN
        INSERT INTO documents_changelog(document_id, old_data, new_data) VALUES (NEW.id, OLD.data, NEW.data);
    ELSIF (TG_OP = 'INSERT') THEN
        INSERT INTO documents_changelog(document_id, old_data, new_data) VALUES (NEW.id, Null, NEW.data);
    END IF;
    RETURN NULL; -- For AFTER triggers, the return value is ignored.
END;
$$ LANGUAGE plpgsql;
​
CREATE TRIGGER emp_audit_trigger
AFTER INSERT OR UPDATE OR DELETE ON documents
FOR EACH ROW EXECUTE FUNCTION audit_log_trigger();
​
​
​
​
​