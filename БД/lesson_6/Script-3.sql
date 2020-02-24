/*
* Определить кто больше поставил лайков (всего) - мужчины или женщины?
*/

use vk;

SELECT 
(select count(*) from
(select likes.user_id, profiles.gender
from likes, profiles
where likes.user_id = profiles.user_id and profiles.gender = 'm') cntm) as man
,

(select count(*) from
(select likes.user_id, profiles.gender
from likes, profiles
where likes.user_id = profiles.user_id and profiles.gender = 'f') cntf) as woman
	

