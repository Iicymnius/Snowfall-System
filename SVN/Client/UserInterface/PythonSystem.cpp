//find;

void CPythonSystem::SetShowSalesTextFlag(int iFlag)

//add above;

#ifdef ENABLE_SHOW_SNOW_SYSTEM
bool CPythonSystem::GetSnowMode()
{
	return m_Config.bSnowMode;
}

void CPythonSystem::SetSnowMode(int iFlag)
{
	m_Config.bSnowMode = iFlag == 1 ? true : false;
}
#endif

//find again;

		else if (!stricmp(command, "SHOW_SALESTEXT"))
			m_Config.bShowSalesText = atoi(value) == 1 ? true : false;

//add below;

#ifdef ENABLE_SHOW_SNOW_SYSTEM
		else if (!stricmp(command, "SNOW_MODE"))
			m_Config.bSnowMode = atoi(value) == 1 ? true : false;
#endif

//find again;

	if (m_Config.bShowSalesText == 0)
		fprintf(fp, "SHOW_SALESTEXT		%d\n", m_Config.bShowSalesText);

//add below;

#ifdef ENABLE_SHOW_SNOW_SYSTEM
	fprintf(fp, "SNOW_MODE				%d\n", m_Config.bSnowMode);
#endif