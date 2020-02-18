/*
 * Подсчитать общее количество лайков, которые получили пользователи младше 10 лет.
 */

use vk;

select sum(cnt) from
	(select media_id, count(*) as 'cnt' from likes where id in
		(select id from media where user_id in
			(select user_id from profiles where TIMESTAMPDIFF(year, birthday, now()) <  10))
	GROUP BY media_id) t