with last_varation_data as (
	select stores_products_id as id, max("snapshot") as "snapshot" 
	from variations
	group by 1
)
, variation as (
	select v.*
	from variations v
	inner join last_varation_data lvd on lvd.id = v.stores_products_id and	v."snapshot" = lvd."snapshot"
)
select r.email, r.comparison_type , r."parameter", v.value as last_price, sp.id as stores_products_id, p.description, sp.api_product_code, s.*
from stores_products sp
inner join stores s on s."name"  = sp.store
inner join products p on p.id  = sp.product_id
inner join receivers r on r.product_id = p.id
left join variation v on v.stores_products_id = sp.id;