//find;

		bool			bShowSalesText;

//add below;

#ifdef ENABLE_SHOW_SNOW_SYSTEM
		bool			bSnowMode;
#endif

//find again;

	void							SetShowSalesTextFlag(int iFlag);

//add below;

#ifdef ENABLE_SHOW_SNOW_SYSTEM
	void							SetSnowMode(int iFlag);
	bool							GetSnowMode();
#endif