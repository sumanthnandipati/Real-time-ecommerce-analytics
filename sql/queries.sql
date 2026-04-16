-- Total Revenue
SELECT SUM(price) AS total_revenue
FROM events
WHERE event_type = 'purchase';

-- Top Products by Revenue
SELECT product_id, SUM(price) AS revenue
FROM events
WHERE event_type = 'purchase'
GROUP BY product_id
ORDER BY revenue DESC
LIMIT 10;

-- User Behavior Distribution
SELECT event_type, COUNT(*) AS total_events
FROM events
GROUP BY event_type;
