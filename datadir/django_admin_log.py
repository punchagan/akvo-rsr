table = 'django_admin_log'
fields = ['id', 'action_time', 'user_id', 'content_type_id', 'object_id', 'object_repr', 'action_flag', 'change_message']
#default item format: "fieldname":("type", "value")
default = {}
records = [
[1, '2008-06-19 23:07:12', 1, 12, u'1', u'The training of vocational students in buildi', 1, u'']
[2, '2008-06-19 23:13:21', 1, 14, u'1', u'Plieger', 1, u'']
[3, '2008-06-19 23:15:05', 1, 12, u'1', u'The training of vocational students in buildi', 2, u'No fields changed.']
[4, '2008-06-19 23:18:53', 1, 12, u'1', u'The training of vocational students in buildi', 2, u'Added funding partner "Plieger 1 EUR".']
[5, '2008-06-19 23:19:14', 1, 12, u'1', u'The training of vocational students in buildi', 2, u'Changed funding amount for funding partner "Plieger 14921 EUR".']
[6, '2008-06-19 23:22:05', 1, 14, u'2', u'Iringa Development of You', 1, u'']
[7, '2008-06-19 23:26:22', 1, 14, u'3', u'WASTE', 1, u'']
[8, '2008-06-19 23:26:33', 1, 12, u'1', u'The training of vocational students in buildi', 2, u'Added field partner "Iringa Development of You" and sponsor partner "WASTE".']
[9, '2008-06-19 23:29:52', 1, 10, u'1', u'19313 EUR', 1, u'']
[10, '2008-06-21 12:15:46', 1, 14, u'3', u'WASTE', 2, u'Changed logo.']
[11, '2008-06-23 17:29:19', 1, 14, u'4', u'Bangladesh Association fo', 1, u'']
[12, '2008-06-23 17:32:39', 1, 14, u'4', u'BASA', 2, u'Changed name, url, postcode, phone and fax.']
[13, '2008-06-23 17:32:40', 1, 14, u'4', u'BASA', 2, u'No fields changed.']
[14, '2008-06-23 17:35:02', 1, 14, u'5', u'PA Bangladesh', 1, u'']
[15, '2008-06-23 17:35:59', 1, 14, u'2', u'IDYDC', 2, u'Changed name and address 1.']
[16, '2008-06-23 17:46:23', 1, 12, u'2', u'Bangladesh ecological sanitation for 5 school', 1, u'']
[17, '2008-06-23 17:46:47', 1, 12, u'2', u'Bangladesh ecological sanitation for 5 school', 2, u'Added sponsor partner "WASTE" and field partner "PA Bangladesh".']
[18, '2008-06-23 17:49:50', 1, 12, u'2', u'Bangladesh ecological sanitation for 5 school', 2, u'Deleted sponsor partner "WASTE".']
[19, '2008-06-23 17:56:46', 1, 10, u'2', u'16000 EUR', 1, u'']
[20, '2008-06-23 21:18:23', 1, 13, u'1', u'ProjectUpdate object', 3, u'']
[21, '2008-06-23 21:18:31', 1, 13, u'12', u'ProjectUpdate object', 3, u'']
[22, '2008-06-23 21:19:23', 1, 13, u'2', u'ProjectUpdate object', 3, u'']
[23, '2008-06-24 12:05:27', 1, 12, u'2', u'Bangladesh ecological sanitation for 5 school', 2, u'Added sponsor partner "WASTE". Changed status.']
[24, '2008-06-24 15:57:37', 1, 18, u'1', u'Akvo blog (http://www.akvo.org/blog/?feed=rss2)', 1, u'']
[25, '2008-06-24 16:02:01', 1, 16, u'1', u'Akvo blog (http://www.akvo.org/blog/?feed=rss2)', 1, u'']
[26, '2008-06-24 16:02:28', 1, 17, u'1', u'Akvo.org', 1, u'']
[27, '2008-06-24 16:30:23', 1, 7, u'1', u'akvo.org', 2, u'Changed domain name and display name.']
[28, '2008-06-24 22:13:15', 1, 3, u'3', u'gino', 2, u'Changed staff status, last login and date joined.']
[29, '2008-06-24 22:14:49', 1, 3, u'4', u'malte', 2, u'Changed staff status, last login and date joined.']
[30, '2008-06-24 22:15:02', 1, 3, u'2', u'thomas', 2, u'Changed staff status, last login and date joined.']
[31, '2008-06-25 13:13:28', 1, 22, u'1', u'ProjectComment object', 1, u'']
[32, '2008-06-25 17:45:44', 1, 3, u'5', u'peter', 2, u'Changed first name, last name, e-mail address, staff status, last login and date joined.']
[33, '2008-06-25 17:50:10', 1, 3, u'6', u'luuk', 2, u'Changed first name, last name, e-mail address, staff status, last login and date joined.']
[34, '2008-06-25 17:50:38', 1, 3, u'1', u'gabriel', 2, u'Changed first name, last name, e-mail address and last login.']
[35, '2008-06-25 17:51:19', 1, 3, u'3', u'gino', 2, u'Changed first name, last name and e-mail address.']
[36, '2008-06-25 17:51:45', 1, 3, u'4', u'malte', 2, u'Changed first name, last name, e-mail address and last login.']
[37, '2008-06-25 17:52:16', 1, 3, u'2', u'thomas', 2, u'Changed first name, last name, e-mail address and last login.']
[38, '2008-06-25 17:53:45', 1, 2, u'1', u'RSR editors', 1, u'']
[39, '2008-06-25 17:54:12', 1, 3, u'3', u'gino', 2, u'No fields changed.']
[40, '2008-06-25 17:54:51', 1, 3, u'6', u'luuk', 2, u'No fields changed.']
[41, '2008-06-25 17:55:47', 1, 3, u'4', u'malte', 2, u'No fields changed.']
[42, '2008-06-25 17:56:05', 1, 3, u'5', u'peter', 2, u'No fields changed.']
[43, '2008-06-25 17:56:16', 1, 3, u'2', u'thomas', 2, u'No fields changed.']
[44, '2008-06-25 17:57:11', 1, 2, u'1', u'RSR editors', 2, u'No fields changed.']
[45, '2008-06-25 17:59:08', 1, 3, u'7', u'beth', 2, u'Changed first name, last name, e-mail address, staff status, last login and date joined.']
[46, '2008-06-27 23:38:44', 1, 12, u'2', u'Bangladesh ecological sanitation for 5 school', 2, u'Changed funding amount for funding partner "Plieger 12000 EUR". Deleted sponsor partner "WASTE".']
[47, '2008-06-30 19:21:37', 1, 14, u'6', u'Simawi', 1, u'']
[48, '2008-06-30 19:23:37', 1, 14, u'7', u'COMMUNITY BASED HEALTH CA', 1, u'']
[49, '2008-06-30 19:25:43', 1, 12, u'3', u'Osunyai School Health and Sanitation Project ', 1, u'']
[50, '2008-06-30 19:29:18', 1, 14, u'8', u'Simawi', 1, u'']
[51, '2008-06-30 19:29:55', 1, 12, u'3', u'Osunyai School Health and Sanitation Project ', 2, u'Added sponsor partner "Simawi".']
[52, '2008-07-01 12:54:51', 1, 14, u'1', u'Plieger', 2, u'Changed funding partner.']
[53, '2008-07-01 12:55:06', 1, 14, u'8', u'Simawi', 2, u'Changed field partner and support partner.']
[54, '2008-07-01 12:55:58', 1, 14, u'7', u'CBHCC', 2, u'Changed field partner, name and long name.']
[55, '2008-07-01 12:56:39', 1, 14, u'8', u'Simawi', 2, u'Changed long name.']
[56, '2008-07-01 12:57:19', 1, 14, u'6', u'Simawi', 3, u'']
[57, '2008-07-01 12:57:34', 1, 14, u'5', u'PA Bangladesh', 2, u'Changed field partner and long name.']
[58, '2008-07-01 12:58:00', 1, 14, u'4', u'BASA', 2, u'Changed field partner and long name.']
[59, '2008-07-01 12:58:19', 1, 14, u'5', u'PA Bangladesh', 2, u'Changed long name.']
[60, '2008-07-01 12:59:47', 1, 14, u'3', u'WASTE', 2, u'Changed support partner and long name.']
[61, '2008-07-01 13:00:14', 1, 14, u'2', u'IDYDC', 2, u'Changed field partner and long name.']
[62, '2008-07-01 13:00:28', 1, 14, u'1', u'Plieger', 2, u'Changed long name.']
[63, '2008-07-01 13:06:46', 1, 14, u'8', u'Simawi', 2, u'Changed field partner and funding partner.']
[64, '2008-07-01 13:07:13', 1, 12, u'3', u'Osunyai School Health and Sanitation Project ', 2, u'Added funding partner "Simawi 10000 EUR" and support partner "Simawi".']
[65, '2008-07-01 13:08:00', 1, 12, u'2', u'Bangladesh ecological sanitation for 5 school', 2, u'Added support partner "WASTE".']
[66, '2008-07-01 13:08:41', 1, 12, u'1', u'The training of vocational students in buildi', 2, u'Added support partner "WASTE".']
[67, '2008-07-02 11:28:33', 1, 14, u'8', u'Simawi', 2, u'Changed description.']
[68, '2008-07-02 11:28:45', 1, 14, u'7', u'CBHCC', 2, u'Changed description.']
[69, '2008-07-02 11:28:57', 1, 14, u'5', u'PA Bangladesh', 2, u'Changed description.']
[70, '2008-07-02 11:29:10', 1, 14, u'4', u'BASA', 2, u'Changed description.']
[71, '2008-07-02 11:29:22', 1, 14, u'4', u'BASA', 2, u'No fields changed.']
[72, '2008-07-02 11:29:29', 1, 14, u'3', u'WASTE', 2, u'Changed description.']
[73, '2008-07-02 11:29:39', 1, 14, u'2', u'IDYDC', 2, u'Changed description.']
[74, '2008-07-02 11:29:58', 1, 14, u'1', u'Plieger', 2, u'Changed description.']
[75, '2008-07-05 01:09:15', 1, 12, u'1', u'The training of vocational students in buildi', 2, u'Changed current image caption and hygiene facilities.']
[76, '2008-07-05 01:16:24', 1, 12, u'1', u'The training of vocational students in buildi', 2, u'Changed current image.']
[77, '2008-07-07 15:16:11', 2, 12, u'2', u'Bangladesh ecological sanitation for 5 school', 2, u'Changed current image caption and hygiene facilities.']
[78, '2008-07-07 15:17:03', 2, 12, u'2', u'Bangladesh ecological sanitation for 5 school', 2, u'Changed current image.']
[79, '2008-07-07 15:21:13', 2, 12, u'3', u'Osunyai School Health and Sanitation Project ', 2, u'Changed current image, current image caption and hygiene facilities.']
[80, '2008-07-07 16:19:25', 2, 13, u'15', u'ProjectUpdate object', 3, u'']
[81, '2008-07-07 16:23:18', 2, 13, u'10', u'ProjectUpdate object', 3, u'']
[82, '2008-07-07 16:25:21', 2, 13, u'9', u'ProjectUpdate object', 2, u'Changed text and photo location.']
[83, '2008-07-07 16:34:06', 2, 22, u'11', u'ProjectComment object', 2, u'Changed comment.']
[84, '2008-07-07 16:37:12', 2, 13, u'18', u'ProjectUpdate object', 3, u'']
[85, '2008-07-07 16:41:40', 2, 13, u'17', u'ProjectUpdate object', 3, u'']
[86, '2008-07-07 16:41:50', 2, 13, u'16', u'ProjectUpdate object', 3, u'']
[87, '2008-07-07 16:42:04', 2, 13, u'11', u'ProjectUpdate object', 3, u'']
[88, '2008-07-07 16:43:36', 2, 13, u'5', u'ProjectUpdate object', 2, u'Changed text and photo location.']
[89, '2008-07-07 16:44:05', 2, 22, u'9', u'ProjectComment object', 3, u'']
[90, '2008-07-07 16:44:18', 2, 22, u'8', u'ProjectComment object', 3, u'']
[91, '2008-07-07 16:45:28', 2, 22, u'10', u'ProjectComment object', 2, u'Changed comment.']
[92, '2008-07-07 16:46:11', 2, 22, u'7', u'ProjectComment object', 2, u'Changed comment.']
[93, '2008-07-08 10:28:50', 2, 12, u'3', u'Osunyai School Health and Sanitation Project ', 2, u'Changed goals summary.']
[94, '2008-07-08 10:30:39', 2, 12, u'3', u'Osunyai School Health and Sanitation Project ', 2, u'Changed subtitle.']
[95, '2008-07-08 10:32:03', 2, 12, u'2', u'Bangladesh ecological sanitation for 5 school', 2, u'Changed subtitle.']
[96, '2008-07-08 10:32:36', 2, 12, u'1', u'The training of vocational students in buildi', 2, u'Changed subtitle.']
[97, '2008-07-08 10:33:33', 2, 12, u'2', u'Bangladesh ecological sanitation for 5 school', 2, u'Changed subtitle.']
[98, '2008-07-08 10:34:29', 2, 12, u'1', u'Training students to build latrines', 2, u'Changed name.']
[99, '2008-07-08 10:35:04', 2, 12, u'3', u'Osunyai school health and sanitation project ', 2, u'Changed name.']
[100, '2008-07-08 11:13:02', 2, 13, u'9', u'ProjectUpdate object', 2, u'Changed title.']
[101, '2008-07-08 11:43:12', 1, 12, u'2', u'Bangladesh ecological sanitation for 5 school', 2, u'Changed funding amount for funding partner "Plieger 16000 EUR".']
[102, '2008-07-10 00:40:04', 2, 14, u'8', u'Simawi', 2, u'Changed organization type, logo and description.']
[103, '2008-07-10 00:41:59', 2, 14, u'8', u'Simawi', 2, u'Changed logo.']
[104, '2008-07-10 00:57:04', 1, 14, u'7', u'CBHCC', 2, u'Changed organization type.']
[105, '2008-07-10 00:57:14', 1, 14, u'5', u'PA Bangladesh', 2, u'Changed organization type.']
[106, '2008-07-10 00:57:21', 1, 14, u'4', u'BASA', 2, u'Changed organization type.']
[107, '2008-07-10 00:57:30', 1, 14, u'3', u'WASTE', 2, u'Changed organization type.']
[108, '2008-07-10 00:57:39', 1, 14, u'2', u'IDYDC', 2, u'Changed organization type.']
[109, '2008-07-10 00:57:47', 1, 14, u'1', u'Plieger', 2, u'Changed organization type.']
[110, '2008-07-10 01:04:36', 2, 14, u'1', u'Plieger', 2, u'Changed logo.']
[111, '2008-07-10 01:05:34', 2, 14, u'1', u'Plieger', 2, u'Changed contact person and contact email.']
[112, '2008-07-10 01:08:51', 2, 14, u'3', u'WASTE', 2, u'Changed logo.']
[113, '2008-07-10 23:01:55', 1, 13, u'5', u'ProjectUpdate object', 2, u'Changed title, photo caption and photo credit.']
[114, '2008-07-11 00:40:49', 1, 13, u'13', u'ProjectUpdate object', 2, u'Changed photo location.']
[115, '2008-07-14 06:37:46', 7, 14, u'9', u'FP: Athos', 1, u'']
[116, '2008-07-14 06:46:46', 7, 14, u'10', u'S: Porthos', 1, u'']
[117, '2008-07-14 06:52:20', 7, 14, u'11', u'M: Aramis', 1, u'']
[118, '2008-07-14 06:56:16', 7, 14, u'12', u'T: Plus One', 1, u'']
[119, '2008-07-14 07:21:03', 7, 14, u'11', u'M: Aramis', 2, u'Changed funding partner.']
[120, '2008-07-14 07:30:34', 7, 14, u'12', u'T: Plus One', 3, u'']
[121, '2008-07-14 18:06:08', 1, 24, u'1', u'Tanzania', 1, u'']
[122, '2008-07-14 18:06:25', 1, 24, u'2', u'India', 1, u'']
[123, '2008-07-14 23:06:41', 1, 24, u'3', u'The Netherlands', 1, u'']
[124, '2008-07-14 23:06:46', 1, 14, u'1', u'Plieger', 2, u'Changed country.']
[125, '2008-07-14 23:07:05', 1, 14, u'3', u'WASTE', 2, u'Changed country.']
[126, '2008-07-14 23:07:24', 1, 24, u'4', u'Bangladesh', 1, u'']
[127, '2008-07-14 23:07:31', 1, 14, u'4', u'BASA', 2, u'Changed country.']
[128, '2008-07-14 23:07:45', 1, 14, u'5', u'PA Bangladesh', 2, u'Changed country.']
[129, '2008-07-14 23:08:12', 1, 14, u'8', u'Simawi', 2, u'Changed country.']
[130, '2008-07-14 23:08:30', 1, 24, u'5', u'USA', 1, u'']
[131, '2008-07-14 23:08:34', 1, 14, u'11', u'M: Aramis', 2, u'Changed country.']
[132, '2008-07-14 23:08:46', 1, 14, u'10', u'S: Porthos', 2, u'Changed country.']
[133, '2008-07-14 23:08:55', 1, 14, u'9', u'FP: Athos', 2, u'Changed country.']
[134, '2008-07-14 23:09:57', 1, 12, u'2', u'Bangladesh ecological sanitation for 5 school', 2, u'Changed country.']
[135, '2008-07-14 23:11:40', 7, 14, u'9', u'FP: Athos', 2, u'Changed support partner, funding partner, logo, address 1, address 2, fax, contact person and description.']
[136, '2008-07-14 23:28:57', 7, 14, u'9', u'Athos', 2, u'Changed name.']
[137, '2008-07-14 23:40:47', 7, 14, u'10', u'Porthos', 2, u'Changed name, address 1, address 2, fax, contact person and description.']
[138, '2008-07-14 23:44:46', 7, 14, u'11', u'Aramis', 2, u'Changed name, state, address 2 and fax.']
[139, '2008-07-15 00:07:10', 7, 14, u'11', u'Aramis', 2, u'Changed field partner and funding partner.']
[140, '2008-07-15 00:29:20', 7, 12, u'4', u'Municipal water reuse / gray water.', 1, u'']
[141, '2008-07-15 01:10:04', 7, 12, u'4', u'Municipal water reuse / gray water.', 2, u'Added support partner "Porthos" and field partner "Aramis".']
[142, '2008-07-15 01:11:05', 7, 12, u'4', u'Municipal water reuse / gray water.', 2, u'No fields changed.']
[143, '2008-07-15 01:11:55', 7, 12, u'4', u'Municipal water reuse / gray water.', 2, u'No fields changed.']
[144, '2008-07-15 01:16:08', 7, 12, u'4', u'Municipal water reuse / gray water.', 2, u'Added funding partner "Athos 200 EUR".']
[145, '2008-07-15 01:24:21', 7, 14, u'9', u'Athos', 2, u'Changed logo.']
[146, '2008-07-15 01:29:31', 7, 14, u'9', u'Athos', 2, u'Changed map.']
[147, '2008-07-15 07:04:17', 7, 12, u'5', u'Mercury', 1, u'']
[148, '2008-07-15 07:05:06', 7, 12, u'5', u'Mercury', 2, u'No fields changed.']
[149, '2008-07-15 07:07:20', 7, 12, u'6', u'Venus', 1, u'']
[150, '2008-07-15 07:08:00', 7, 12, u'6', u'Venus', 2, u'Changed category maintenance.']
[151, '2008-07-15 07:09:41', 7, 12, u'7', u'Mars', 1, u'']
[152, '2008-07-15 07:11:03', 7, 12, u'8', u'Saturn', 1, u'']
[153, '2008-07-15 07:12:38', 7, 12, u'9', u'Jupiter', 1, u'']
[154, '2008-07-15 07:14:08', 7, 12, u'10', u'Uranus', 1, u'']
[155, '2008-07-15 07:15:24', 7, 12, u'11', u'Neptune', 1, u'']
[156, '2008-07-15 07:18:16', 7, 12, u'12', u'Pluto', 1, u'']
[157, '2008-07-15 07:23:23', 7, 12, u'13', u'Add me', 1, u'']
[158, '2008-07-15 14:30:07', 6, 14, u'12', u'CUS', 1, u'']
[159, '2008-07-15 14:37:58', 6, 12, u'14', u'School Sanitation in Rural Areas', 1, u'']
[160, '2008-07-15 14:39:46', 6, 14, u'12', u'CUS', 2, u'Changed field partner.']
[161, '2008-07-15 14:40:10', 6, 12, u'14', u'School Sanitation in Rural Areas', 2, u'Added field partner "CUS".']
[162, '2008-07-15 14:40:50', 6, 12, u'14', u'School Sanitation in Rural Areas', 2, u'No fields changed.']
[163, '2008-07-15 14:55:39', 6, 12, u'14', u'School Sanitation in Rural Areas', 2, u'No fields changed.']
[164, '2008-07-15 15:24:21', 6, 12, u'15', u'School sanitation in peri-urban area', 1, u'']
[165, '2008-07-15 15:30:19', 6, 14, u'13', u'WASTE', 1, u'']
[166, '2008-07-15 15:34:32', 6, 14, u'14', u'FODRA', 1, u'']
[167, '2008-07-15 15:50:58', 6, 12, u'15', u'School sanitation in peri-urban area', 2, u'Changed current image.']
[168, '2008-07-15 15:54:42', 6, 12, u'15', u'School sanitation in peri-urban area', 2, u'Changed current image.']
[169, '2008-07-15 15:59:29', 6, 12, u'15', u'School sanitation in peri-urban area', 2, u'Added support partner "WASTE" and field partner "FODRA". Changed current image, sanitation systems and improved water.']
[170, '2008-07-15 16:05:46', 6, 12, u'15', u'School sanitation in peri-urban area', 2, u'No fields changed.']
[171, '2008-07-15 16:08:34', 6, 12, u'15', u'School sanitation in peri-urban area', 2, u'No fields changed.']
[172, '2008-07-15 16:09:39', 6, 14, u'14', u'FODRA', 2, u'Changed logo.']
[173, '2008-07-15 16:23:42', 6, 12, u'15', u'School sanitation in peri-urban area', 2, u'Added funding partner "WASTE 8000 EUR". Changed sustainability.']
[174, '2008-07-15 16:59:24', 6, 14, u'3', u'WASTE', 3, u'']
[175, '2008-07-15 18:21:24', 7, 12, u'13', u'Add me', 3, u'']
[176, '2008-07-15 18:32:53', 7, 12, u'16', u'Add after subtract test', 1, u'']
[177, '2008-07-15 18:33:13', 7, 12, u'16', u'Add after subtract test', 2, u'No fields changed.']
[178, '2008-07-15 18:35:29', 7, 12, u'16', u'Add after subtract test', 3, u'']
[179, '2008-07-15 18:44:46', 7, 12, u'11', u'Neptune', 3, u'']
[180, '2008-07-15 18:45:03', 7, 12, u'10', u'Uranus', 3, u'']
[181, '2008-07-15 18:48:06', 7, 12, u'9', u'Jupiter', 3, u'']
[182, '2008-07-15 19:08:30', 7, 12, u'5', u'Mercury', 2, u'Added funding partner "Athos 2000 USD". Changed subtitle, goal 1, goal 2 and goal 3.']
[183, '2008-07-15 19:11:48', 7, 12, u'5', u'Mercury', 2, u'Added support partner "Porthos" and field partner "Aramis". Changed context.']
[184, '2008-07-15 19:13:47', 7, 12, u'5', u'Mercury', 2, u'Changed project plan summary.']
[185, '2008-07-15 19:26:15', 7, 13, u'17', u'ProjectUpdate object', 1, u'']
[186, '2008-07-15 19:29:14', 7, 13, u'17', u'ProjectUpdate object', 2, u'Changed photo.']
[187, '2008-07-16 09:42:54', 2, 14, u'12', u'CUS', 2, u'Changed logo.']
[188, '2008-07-16 09:43:41', 2, 14, u'7', u'CBHCC', 2, u'Changed long name.']
[189, '2008-07-16 09:45:29', 2, 12, u'12', u'TEST Pluto', 2, u'Changed name.']
[190, '2008-07-16 09:45:42', 2, 12, u'8', u'TEST Saturn', 2, u'Changed name.']
[191, '2008-07-16 09:45:55', 2, 12, u'7', u'TEST Mars', 2, u'Changed name.']
[192, '2008-07-16 09:46:08', 2, 12, u'6', u'TEST Venus', 2, u'Changed name.']
[193, '2008-07-16 09:46:21', 2, 12, u'5', u'TEST Mercury', 2, u'Changed name.']
[194, '2008-07-16 09:48:36', 2, 12, u'4', u'TEST Municipal water reuse / gray water.', 2, u'Changed name.']
[195, '2008-07-16 10:01:53', 6, 14, u'15', u'PRACTICA', 1, u'']
[196, '2008-07-16 10:16:41', 6, 14, u'16', u'CRS', 1, u'']
[197, '2008-07-16 10:24:29', 6, 12, u'16', u'Low cost rehabilitation of impluvia', 1, u'']
[198, '2008-07-16 10:25:22', 6, 12, u'16', u'Low cost rehabilitation of impluvia', 2, u'Changed goals summary.']
[199, '2008-07-16 10:28:43', 6, 12, u'16', u'Low cost rehabilitation of impluvia', 2, u'No fields changed.']
[200, '2008-07-16 10:30:35', 6, 12, u'16', u'Low cost rehabilitation of impluvia', 2, u'Changed country.']
[201, '2008-07-16 10:45:19', 6, 14, u'17', u'VSA', 1, u'']
[202, '2008-07-16 10:48:15', 6, 12, u'17', u'Training on manual drilling', 1, u'']
[203, '2008-07-16 10:48:38', 6, 14, u'17', u'VSA', 2, u'No fields changed.']
[204, '2008-07-16 10:49:09', 6, 12, u'17', u'Training on manual drilling', 2, u'Added field partner "VSA".']
[205, '2008-07-16 10:57:07', 6, 12, u'18', u'Product Development/Marketing of a UD toilet ', 1, u'']
[206, '2008-07-16 10:58:31', 6, 12, u'18', u'Product Development/ Marketing of UD toilets ', 2, u'Changed name.']
[207, '2008-07-16 11:10:58', 6, 14, u'18', u'FSG', 1, u'']
[208, '2008-07-16 11:12:15', 6, 12, u'19', u'Improvement of Water filter Production', 1, u'']
[209, '2008-07-16 11:14:05', 6, 12, u'19', u'Improvement of Water filter Production', 2, u'Changed project plan detail.']
[210, '2008-07-16 11:16:38', 6, 12, u'19', u'Improvement of Water filter Production', 2, u'Changed goal 1.']
[211, '2008-07-16 11:59:23', 6, 12, u'20', u'Vocational student training in Tanzania', 1, u'']
[212, '2008-07-16 12:08:10', 1, 12, u'12', u'TEST Pluto', 2, u'Added link "http://www.akvo.org/wiki/".']
[213, '2008-07-16 12:09:04', 1, 12, u'12', u'TEST Pluto', 2, u'Added link "http://www.waste.nl/".']
[214, '2008-07-16 12:12:17', 6, 12, u'14', u'School Sanitation in Rural Areas', 2, u'Changed goal 1, goal 2 and goal 3.']
[215, '2008-07-16 12:13:20', 6, 12, u'14', u'School Sanitation in Rural Areas', 2, u'Changed goal 1, goal 2 and goal 3.']
[216, '2008-07-16 12:19:37', 1, 12, u'12', u'TEST Pluto', 2, u'Added link "http://www.irc.nl".']
[217, '2008-07-16 12:37:22', 1, 2, u'1', u'RSR editors', 2, u'No fields changed.']
[218, '2008-07-16 13:45:37', 6, 24, u'6', u'Madagascar', 1, u'']
[219, '2008-07-16 13:45:57', 6, 12, u'17', u'Training on manual drilling', 2, u'Changed country.']
[220, '2008-07-16 13:46:12', 6, 12, u'16', u'Low cost rehabilitation of impluvia', 2, u'Changed country.']
[221, '2008-07-16 13:53:16', 6, 10, u'5', u'School sanitation in peri-urban area', 1, u'']
[222, '2008-07-16 13:59:48', 6, 10, u'5', u'School sanitation in peri-urban area', 3, u'']
[223, '2008-07-16 14:01:28', 6, 10, u'5', u'School sanitation in peri-urban area', 1, u'']
[224, '2008-07-16 14:03:17', 6, 10, u'6', u'Low cost rehabilitation of impluvia', 1, u'']
[225, '2008-07-16 14:05:21', 6, 10, u'7', u'Training on manual drilling', 1, u'']
[226, '2008-07-16 14:06:36', 6, 10, u'8', u'Product Development/ Marketing of UD toilets ', 1, u'']
[227, '2008-07-16 14:07:22', 6, 10, u'9', u'Improvement of Water filter Production', 1, u'']
[228, '2008-07-16 14:08:57', 6, 10, u'10', u'Vocational student training in Tanzania', 1, u'']
[229, '2008-07-16 14:11:33', 6, 12, u'19', u'Improvement of Water filter Production', 2, u'Changed country.']
[230, '2008-07-16 14:12:53', 6, 14, u'8', u'Simavi', 2, u'Changed name.']
[231, '2008-07-16 14:14:20', 6, 14, u'16', u'CRS', 2, u'Changed logo.']
[232, '2008-07-16 14:18:51', 6, 14, u'1', u'Plieger', 2, u'Changed logo.']
[233, '2008-07-16 14:30:13', 6, 14, u'19', u'BASA', 1, u'']
[234, '2008-07-16 14:33:42', 6, 14, u'20', u'PA Bangladesh', 1, u'']
[235, '2008-07-16 14:39:16', 6, 24, u'7', u'Burkina Faso', 1, u'']
[236, '2008-07-16 14:39:36', 6, 14, u'21', u'Sahel Solidarit\xe9', 1, u'']
[237, '2008-07-16 14:43:10', 6, 24, u'8', u'Cameroon', 1, u'']
[238, '2008-07-16 14:44:37', 6, 14, u'22', u'ADEID', 1, u'']
[239, '2008-07-16 14:48:20', 6, 14, u'23', u'CBHCC', 1, u'']
[240, '2008-07-16 14:50:17', 6, 14, u'13', u'WASTE', 2, u'Changed logo.']
[241, '2008-07-16 14:54:28', 6, 14, u'24', u'CUS', 1, u'']
[242, '2008-07-16 14:54:50', 6, 14, u'24', u'CUS', 2, u'Changed field partner.']
[243, '2008-07-16 14:55:14', 6, 14, u'8', u'Simavi', 2, u'Changed field partner.']
[244, '2008-07-16 14:55:27', 6, 14, u'15', u'PRACTICA', 2, u'Changed field partner and funding partner.']
[245, '2008-07-16 15:01:15', 6, 24, u'9', u'Nepal', 1, u'']
[246, '2008-07-16 15:03:00', 6, 14, u'25', u'ENPHO', 1, u'']
[247, '2008-07-16 15:04:28', 6, 14, u'24', u'CUS', 2, u'Changed logo.']
[248, '2008-07-16 15:08:13', 6, 14, u'24', u'CUS', 3, u'']
[249, '2008-07-16 15:11:05', 6, 24, u'10', u'Malawi', 1, u'']
[250, '2008-07-16 15:11:53', 6, 14, u'26', u'Hygiene Village Project', 1, u'']
[251, '2008-07-16 15:15:54', 6, 24, u'11', u'Ghana', 1, u'']
[252, '2008-07-16 15:17:47', 6, 14, u'27', u'Simli AiD', 1, u'']
[253, '2008-07-16 15:21:26', 6, 14, u'27', u'Simli AiD', 2, u'Changed field partner, url and map.']
[254, '2008-07-16 15:21:39', 6, 14, u'26', u'Hygiene Village Project', 2, u'Changed field partner.']
[255, '2008-07-16 15:23:37', 6, 14, u'27', u'Simli AiD', 2, u'Changed logo.']
[256, '2008-07-16 15:26:14', 6, 24, u'12', u'Ehtiopia', 1, u'']
[257, '2008-07-16 15:26:44', 6, 24, u'12', u'Ethiopia', 2, u'Changed country name.']
[258, '2008-07-16 15:29:59', 6, 14, u'28', u'ERHA', 1, u'']
[259, '2008-07-16 15:32:21', 6, 14, u'28', u'ERHA', 2, u'Changed logo.']
[260, '2008-07-16 15:32:47', 6, 14, u'28', u'ERHA', 2, u'Changed logo.']
[261, '2008-07-16 15:33:32', 6, 14, u'28', u'ERHA', 2, u'Changed logo.']
[262, '2008-07-16 15:37:37', 6, 14, u'28', u'ERHA', 2, u'Changed field partner.']
[263, '2008-07-16 15:39:53', 6, 14, u'14', u'FODRA', 2, u'Changed logo.']
[264, '2008-07-16 15:40:52', 6, 14, u'14', u'FODRA', 2, u'Changed logo.']
[265, '2008-07-16 15:42:00', 6, 14, u'14', u'FODRA', 2, u'Changed logo.']
[266, '2008-07-16 15:44:22', 6, 14, u'14', u'FODRA', 2, u'Changed logo.']
[267, '2008-07-16 15:45:32', 6, 14, u'14', u'FODRA', 2, u'Changed logo.']
[268, '2008-07-16 15:46:41', 6, 14, u'15', u'PRACTICA', 2, u'Changed logo.']
[269, '2008-07-16 15:49:30', 6, 14, u'17', u'VSA', 2, u'Changed logo.']
[270, '2008-07-16 15:52:33', 6, 14, u'18', u'FSG', 2, u'Changed logo.']
[271, '2008-07-16 15:55:44', 6, 14, u'22', u'ADEID', 2, u'Changed logo.']
[272, '2008-07-16 15:58:55', 6, 14, u'22', u'ADEID', 2, u'Changed logo.']
[273, '2008-07-16 16:07:08', 6, 24, u'13', u'France', 1, u'']
[274, '2008-07-16 16:08:21', 6, 14, u'29', u'ESF', 1, u'']
[275, '2008-07-16 16:20:52', 6, 24, u'14', u'Armenia', 1, u'']
[276, '2008-07-16 16:22:35', 6, 14, u'30', u'Lore Eco Club', 1, u'']
[277, '2008-07-16 16:23:55', 6, 24, u'15', u'Romania', 1, u'']
[278, '2008-07-16 16:26:34', 6, 14, u'31', u'FVC', 1, u'']
[279, '2008-07-16 16:26:50', 6, 14, u'29', u'ESF', 2, u'Changed field partner and support partner.']
[280, '2008-07-16 16:30:22', 6, 24, u'16', u'Georgia', 1, u'']
[281, '2008-07-16 16:31:08', 6, 14, u'32', u'RCDA', 1, u'']
[282, '2008-07-16 16:31:19', 6, 14, u'30', u'Lore Eco Club', 2, u'Changed logo.']
[283, '2008-07-16 16:34:46', 6, 24, u'17', u'Ukraine', 1, u'']
[284, '2008-07-16 16:35:38', 6, 14, u'33', u'Vozrojdeny', 1, u'']
[285, '2008-07-16 16:51:19', 6, 14, u'34', u'IICD', 1, u'']
[286, '2008-07-16 16:52:06', 6, 14, u'34', u'IICD', 2, u'Changed support partner, contact person and contact email.']
[287, '2008-07-16 16:57:01', 6, 14, u'34', u'IICD', 2, u'Changed field partner and funding partner.']
[288, '2008-07-16 16:59:26', 6, 14, u'35', u'RAIN foundation', 1, u'']
[289, '2008-07-16 17:01:22', 6, 14, u'35', u'RAIN foundation', 2, u'Changed logo.']
[290, '2008-07-16 17:18:44', 6, 12, u'15', u'School sanitation in peri-urban area', 2, u'Changed current image.']
[291, '2008-07-16 17:22:47', 6, 12, u'14', u'School Sanitation in Rural Areas', 2, u'Changed current image.']
[292, '2008-07-16 17:25:48', 6, 12, u'16', u'Low cost rehabilitation of impluvia', 2, u'Changed current image.']
[293, '2008-07-16 17:30:48', 6, 12, u'17', u'Training on manual drilling', 2, u'Changed current image.']
[294, '2008-07-16 17:36:24', 6, 12, u'19', u'Improvement of Water filter Production', 2, u'Changed current image.']
[295, '2008-07-16 17:44:27', 6, 12, u'20', u'Vocational student training in Tanzania', 2, u'Changed current image.']
[296, '2008-07-17 10:03:59', 6, 14, u'36', u'WECF', 1, u'']
[297, '2008-07-17 10:08:23', 6, 12, u'15', u'School sanitation in peri-urban area', 2, u'Added support partner "WASTE".']
[298, '2008-07-17 10:33:43', 6, 14, u'37', u'GRET', 1, u'']
[299, '2008-07-17 10:42:41', 6, 12, u'21', u'Mechanical Proportional Chlorination system', 1, u'']
[300, '2008-07-17 10:48:17', 6, 10, u'11', u'Mechanical Proportional Chlorination system', 1, u'']
[301, '2008-07-17 11:00:23', 6, 14, u'35', u'RAIN foundation', 2, u'Changed logo.']
[302, '2008-07-17 11:02:34', 6, 14, u'35', u'RAIN foundation', 2, u'Changed logo.']
[303, '2008-07-17 11:08:52', 6, 12, u'17', u'Training on manual drilling', 2, u'No fields changed.']
[304, '2008-07-17 11:10:25', 6, 12, u'21', u'Mechanical Proportional Chlorination system', 2, u'Changed current image.']
[305, '2008-07-17 11:34:55', 6, 12, u'22', u'Ecological sanitation for schools(Bangladesh)', 1, u'']
[306, '2008-07-17 11:38:17', 6, 12, u'22', u'Ecological sanitation for schools(Bangladesh)', 2, u'Added field partner "PA Bangladesh".']
[307, '2008-07-17 11:47:07', 6, 12, u'18', u'Product Development/ Marketing of UD toilets ', 2, u'Changed current image.']
[308, '2008-07-17 11:51:09', 6, 12, u'16', u'Low cost rehabilitation of impluvia', 2, u'Changed goals summary.']
[309, '2008-07-17 11:51:56', 6, 12, u'23', u"Syst\xe8me d'information sur l'hygi\xe8ne... ", 1, u'']
[310, '2008-07-17 12:01:51', 6, 12, u'24', u'Startup ceramic water filter production', 1, u'']
[311, '2008-07-17 12:09:50', 6, 12, u'25', u'Osunyai School Health and Sanitation Project ', 1, u'']
[312, '2008-07-17 12:35:14', 6, 12, u'26', u'School Sanitation and Hygiene Education', 1, u'']
[313, '2008-07-17 13:41:29', 1, 2, u'2', u'RSR users', 1, u'']
[314, '2008-07-17 13:46:21', 6, 12, u'27', u'Mudi-Namisa Schools Sanitation Project', 1, u'']
[315, '2008-07-17 14:06:23', 6, 12, u'28', u'Building Sanitation culture in basic schools', 1, u'']
[316, '2008-07-17 14:16:44', 2, 14, u'25', u'ENPHO', 2, u'Changed logo.']
[317, '2008-07-17 14:21:44', 6, 12, u'29', u'Provision of income by harvesting rainwater', 1, u'']
[318, '2008-07-17 14:41:45', 1, 12, u'1', u'Training students to build latrines', 2, u'Changed goal 2 and goal 3.']
[319, '2008-07-17 15:02:45', 6, 14, u'38', u'CRAID', 1, u'']
[320, '2008-07-17 15:04:29', 6, 12, u'30', u'Training on a.o. drilling in Vangaindrano', 1, u'']
[321, '2008-07-17 15:05:22', 6, 12, u'30', u'Training on manual drilling in Vangaindrano', 2, u'Changed name.']
[322, '2008-07-17 15:06:06', 1, 12, u'1', u'Training students to build latrines', 2, u'Added funding partner "WASTE 4711 EUR".']
[323, '2008-07-17 15:06:30', 1, 12, u'1', u'Training students to build latrines', 2, u'Deleted funding partner "WASTE 4711 EUR".']
[324, '2008-07-17 15:06:37', 6, 14, u'39', u'CRAID', 1, u'']
[325, '2008-07-17 15:06:54', 6, 12, u'30', u'Training on manual drilling in Vangaindrano', 2, u'Added funding partner "Athos 10000 EUR" and field partner "CRAID".']
[326, '2008-07-17 15:07:20', 6, 12, u'30', u'Training on manual drilling in Vangaindrano', 2, u'Deleted funding partner "Athos 10000 EUR".']
]
