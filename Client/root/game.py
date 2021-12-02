#find;

		self.currentCubeNPC = 0

#add below;

		if app.ENABLE_SHOW_SNOW_SYSTEM:
			if systemSetting.GetSnowMode():
				systemSetting.SetSnowMode(True)
				background.EnableSnow(1, constInfo.ENVIRONMENT_SNOW)
				background.SetEnvironmentData(1)
			else:
				systemSetting.SetSnowMode(False)
				background.EnableSnow(0, constInfo.ENVIRONMENT_SNOW)
				background.SetEnvironmentData(0)