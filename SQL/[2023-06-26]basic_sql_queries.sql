-- Q1: The ten best-selling video games
SELECT *
FROM game_sales
ORDER BY games_sold DESC
LIMIT 10;

-- Q2: Missing review scores
SELECT COUNT(*)
FROM game_sales as g
LEFT JOIN reviews as r
USING(game)
WHERE (critic_score IS NULL) AND (user_score IS NULL);

-- Q3: Years that video game critics loved
SELECT g.year, ROUND(AVG(r.critic_score), 2) AS avg_critic_score
FROM game_sales AS g
INNER JOIN reviews AS r
USING(game)
GROUP BY g.year
ORDER BY ROUND(AVG(critic_score), 2) DESC
LIMIT 10;

-- Q4: Was 1982 really that great?
SELECT g.year, 
       ROUND(AVG(r.critic_score), 2) AS avg_critic_score, 
       COUNT(*) AS num_games
FROM game_sales AS g
INNER JOIN reviews AS r
USING(game)
GROUP BY g.year
HAVING COUNT(*) > 4
ORDER BY ROUND(AVG(r.critic_score), 2) DESC
LIMIT 10;

-- Q5: Years that dropped off the critics' favorites list¶
SELECT year, 
    avg_critic_score
FROM top_critic_years
EXCEPT
SELECT year, avg_critic_score
FROM top_critic_years_more_than_four_games
ORDER BY avg_critic_score DESC;

-- Q6: Years video game players loved
SELECT g.year, 
       ROUND(AVG(r.user_score), 2) AS avg_user_score, 
       COUNT(*) AS num_games
FROM game_sales AS g
INNER JOIN reviews AS r
USING(game)
GROUP BY g.year
HAVING COUNT(*) > 4
ORDER BY ROUND(AVG(r.user_score), 2) DESC
LIMIT 10;

-- Q7: Years that both players and critics loved¶
SELECT year
FROM top_critic_years_more_than_four_games
INTERSECT
SELECT year
FROM top_user_years_more_than_four_games

--Q8: Sales in the best video game years
SELECT year, 
    SUM(games_sold) AS total_games_sold
FROM game_sales
WHERE year IN (
    SELECT year
    FROM top_critic_years_more_than_four_games
    INTERSECT
    SELECT year
    FROM top_user_years_more_than_four_games
    )
GROUP BY year
ORDER BY total_games_sold DESC
