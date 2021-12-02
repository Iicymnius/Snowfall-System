#find;

	"height" : xx,

#change;

	"height" : xx + 25,

#find again;

			"height" : xx,

#change;

			"height" : xx + 25,

#find again;

				{
					"name" : "fog_level2",
					"type" : "radio_button",

					"x" : 110 + 100,
					"y" : 160,

					"text" : uiScriptLocale.OPTION_FOG_LIGHT,
					
					"default_image" : ROOT_PATH + "small_Button_01.sub",
					"over_image" : ROOT_PATH + "small_Button_02.sub",
					"down_image" : ROOT_PATH + "small_Button_03.sub",
				},

#add below;

				# if app.ENABLE_SHOW_SNOW_SYSTEM:
				{
					"name" : "snow_mode",
					"type" : "text",

					"x" : 40 + TEXT_TEMPORARY_X,
					"y" : 185,

					"text" : "Kar Yaðýþý",
				},
				{
					"name" : "snow_on",
					"type" : "radio_button",

					"x" : 110+70,
					"y" : 185,

					"text" : "Aktif",

					"default_image" : ROOT_PATH + "middle_Button_01.sub",
					"over_image" : ROOT_PATH + "middle_Button_02.sub",
					"down_image" : ROOT_PATH + "middle_Button_03.sub",
				},
				{
					"name" : "snow_off",
					"type" : "radio_button",

					"x" : 110,
					"y" : 185,

					"text" : "Deaktif",
					
					"default_image" : ROOT_PATH + "middle_Button_01.sub",
					"over_image" : ROOT_PATH + "middle_Button_02.sub",
					"down_image" : ROOT_PATH + "middle_Button_03.sub",
				},