/*
 * Пусть задан некоторый пользователь. 
 * Из всех друзей этого пользователя найдите человека, который больше всех общался с нашим пользователем.
 * 
 */

use vk;

-- группируем полученную таблицу по id и считаем сумму сообщений для какждого id
SELECT id FROM (
	-- находим сообщения, где выбранный пользователь получатель, группируем по id и кол-ву сообщений
	SELECT from_user_id as 'id', count(*) as 'cnt' from messages where from_user_id in 	
			
				-- находим друзей
				(SELECT target_user_id FROM friend_requests WHERE initiator_user_id = 1 and status = 'approved'
				UNION 
				SELECT initiator_user_id FROM friend_requests WHERE target_user_id = 1  and status = 'approved') 
	and to_user_id = 1 GROUP BY from_user_id
				
	union
	-- находим сообщния гд выбранный пользователь отправитель, группируем по id и кол-ву сообщений
	SELECT to_user_id as 'id', count(*) as 'cnt' from messages WHERE to_user_id in 
			
				-- находим друзей
				(SELECT target_user_id FROM friend_requests WHERE initiator_user_id = 1 and status = 'approved'
				UNION 
				SELECT initiator_user_id FROM friend_requests WHERE target_user_id = 1  and status = 'approved') 
	and from_user_id = 1 GROUP BY to_user_id) 
t GROUP BY id order by id desc limit 1
