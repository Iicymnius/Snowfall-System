//find;

void initsystemSetting()

//add above;

#ifdef ENABLE_SHOW_SNOW_SYSTEM
PyObject* systemGetSnowMode(PyObject* poSelf, PyObject* poArgs)
{
	return Py_BuildValue("i", CPythonSystem::Instance().GetSnowMode());
}

PyObject* systemSetSnowMode(PyObject* poSelf, PyObject* poArgs)
{
	int iFlag;
	if (!PyTuple_GetInteger(poArgs, 0, &iFlag))
		return Py_BuildException();

	CPythonSystem::Instance().SetSnowMode(iFlag);

	return Py_BuildNone();
}
#endif

//find again;

		{ NULL,							NULL,							NULL }

//add above;

#ifdef ENABLE_SHOW_SNOW_SYSTEM
		{ "GetSnowMode",				systemGetSnowMode,				METH_VARARGS },
		{ "SetSnowMode",				systemSetSnowMode,				METH_VARARGS },
#endif