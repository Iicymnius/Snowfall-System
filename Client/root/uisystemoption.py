#find;

		self.__Load()

#add below;

		if app.ENABLE_SHOW_SNOW_SYSTEM:
			self.RefreshSnowOption()

#find again;

		self.fogModeButtonList = []

#add below;

		if app.ENABLE_SHOW_SNOW_SYSTEM:
			self.snowModeOptionButtonList = []

#find again;

			self.fogModeButtonList.append(GetObject("fog_level2"))

#add below;

			if app.ENABLE_SHOW_SNOW_SYSTEM:
				self.snowModeOptionButtonList.append(GetObject("snow_on"))
				self.snowModeOptionButtonList.append(GetObject("snow_off"))

#find again;

		self.fogModeButtonList[2].SAFE_SetEvent(self.__OnClickFogModeLevel2Button)

#add below;

		if app.ENABLE_SHOW_SNOW_SYSTEM:
			self.snowModeOptionButtonList[0].SAFE_SetEvent(self.__OnClickSnowModeOptionEnableButton)
			self.snowModeOptionButtonList[1].SAFE_SetEvent(self.__OnClickSnowModeOptionDisableButton)

#find again;

	def OnCloseInputDialog(self):

#add above;

	if app.ENABLE_SHOW_SNOW_SYSTEM:
		def __OnClickSnowModeOptionEnableButton(self):
			systemSetting.SetSnowMode(True)
			background.EnableSnow(1, constInfo.ENVIRONMENT_SNOW)
			self.RefreshSnowOption()

		def __OnClickSnowModeOptionDisableButton(self):
			systemSetting.SetSnowMode(False)
			background.EnableSnow(0, constInfo.ENVIRONMENT_SNOW)
			self.RefreshSnowOption()

		def RefreshSnowOption(self):
			if systemSetting.GetSnowMode():
				self.snowModeOptionButtonList[0].Down()
				self.snowModeOptionButtonList[1].SetUp()
			else:
				self.snowModeOptionButtonList[0].SetUp()
				self.snowModeOptionButtonList[1].Down()
