SELECT *, (t.Quantity * t.UnitPrice) AS TotalPrice
FROM online_retail AS t 
WHERE CustomerID IS NOT NULL 
AND t.Quantity > 0
AND t.UnitPrice >0
AND t.StockCode NOT IN ('POST', 'PADS', 'DOT', 'M', 'BANK CHARGES');