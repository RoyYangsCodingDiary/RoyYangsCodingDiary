-- Checks
WITH schema_check AS (
	SELECT column_name, data_type, udt_name
	FROM INFORMATION_SCHEMA.COLUMNS
),

-- Check permissions
permission_check AS (
	SELECT *
	FROM information_schema.table_privileges
	WHERE table_schema = 'public' AND grantee = current_user
)

SELECT *
FROM schema_check;

-- Queries

WITH sub AS (
	SELECT industry
	FROM industries AS i
	INNER JOIN dates AS d
	USING(company_id)
	WHERE EXTRACT(year FROM d.date_joined) IN (2019, 2020, 2021)
	GROUP BY industry
	ORDER BY COUNT(*) DESC
	LIMIT 3
), unicorn_stats AS (
	SELECT
		industry,
		EXTRACT(year FROM date_joined) AS year,
		COUNT(*) AS num_unicorns,
		ROUND(AVG(valuation/1000000000.0), 2) AS average_valuation_billions,
		RANK() OVER (PARTITION BY EXTRACT(year FROM date_joined) ORDER BY COUNT(*) DESC) AS rank_by_year
	FROM dates AS d
	INNER JOIN funding AS f
	USING(company_id)
	INNER JOIN industries AS i
	USING(company_id)
	WHERE EXTRACT(year FROM d.date_joined) IN (2019, 2020, 2021) 
		AND industry IN (SELECT industry FROM sub)
	GROUP BY year, industry
)
SELECT
	industry,
	year,
	num_unicorns,
	average_valuation_billions,
	RANK() OVER (PARTITION BY year ORDER BY num_unicorns DESC) AS rank_within_year,
	(SELECT industry FROM unicorn_stats WHERE year = u.year AND rank_by_year = 1) AS top_industry_by_year
FROM unicorn_stats AS u
ORDER BY industry DESC, year DESC;
