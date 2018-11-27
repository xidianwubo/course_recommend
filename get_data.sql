select stu_id,a.course_id,1 as rating, 20 as timestamp from 
(
	select  stu_id,course_id,1 as rating, 20 as timestamp 
	from sds_stu_buy_course_infos  where dt=20181122 and 
	((year_id=18 and term_id in(1,4)) or year_id>18) 
)a
join
(
	select aa.course_id from 
	(
		select id as course_id from ods_dim_course_v5 where dt=20181122
		and category in(6,7,8,9) and status=2 and is_nosale=0 and is_recommend=1
		and price>0 and  grade_digits>0 and subject_digits>0
	)aa
	join
	(
		select course_id from ods_course_saletimes_v5 where dt=20181125
		and halt_sale_time>='2018-11-26 00:00:00' and status=1
		and sale_time<='2018-11-26 00:00:00'
	)bb on aa.course_id =bb.course_id
)b on a.course_id=b.course_id

