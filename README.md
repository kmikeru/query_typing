Решение задачи 1:

select e.id, e.name, t1.arr from employees e,
    (
        WITH RECURSIVE subordinates AS (
        SELECT
            id,
            parent_id,
            array[id] as ids
        FROM
            departments
        UNION
            SELECT
                e.id,
                e.parent_id,
                ids || e.id
            FROM
                departments e
            INNER JOIN subordinates s ON s.parent_id = e.id
        )
        select id, array_agg(u) as arr from (
            SELECT distinct id, unnest(ids) as u FROM subordinates order by id, u
        ) t group by id
    ) t1
    where e.department_id=t1.id order by e.id;
