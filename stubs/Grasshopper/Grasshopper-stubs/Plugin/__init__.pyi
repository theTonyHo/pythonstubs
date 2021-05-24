from typing import Tuple, Set, Iterable, List


class Commands:
    @property
    def BakeDocument() -> GH_Document: ...
    @property
    def BakeObject() -> IGH_ActiveObject: ...
    def Run_Grasshopper() -> bool: ...
    def Run_GrasshopperBake() -> bool: ...
    def Run_GrasshopperDeveloperSettings() -> bool: ...
    def Run_GrasshopperExportHelp() -> bool: ...
    def Run_GrasshopperFolders() -> bool: ...
    def Run_GrasshopperGetSDKDocumentation() -> bool: ...
    @overload
    def Run_GrasshopperOpen() -> bool: ...
    @overload
    def Run_GrasshopperOpen(path: str) -> bool: ...
    def Run_GrasshopperReloadAssemblies() -> List: ...
    def Run_GrasshopperScripted() -> bool: ...
    def Run_GrasshopperUnloadPlugin() -> bool: ...
    @BakeDocument.setter
    def BakeDocument(Value: GH_Document) -> None: ...
    @BakeObject.setter
    def BakeObject(Value: IGH_ActiveObject) -> None: ...


class GH_PluginUtil:
    def BringRhinoToTop() -> None: ...
    def BringWindowToTop(hWnd: IntPtr) -> bool: ...
    def FocusOnRhino() -> None: ...
    def LoadGrasshopper(message: str) -> Tuple[bool, str]: ...
    def SaveSettings() -> None: ...
    @overload
    def SendKeyCodeToRhino(key: int) -> None: ...
    @overload
    def SendKeyCodeToRhino(key: Char) -> None: ...
    @overload
    def SendKeyCodeToRhino(key: str) -> None: ...
    def SendMessage(hWnd: IntPtr, msg: int, wParam: int, lParam: IntPtr) -> IntPtr: ...
    def SetFocus(hWnd: IntPtr) -> None: ...
    def UnloadGrasshopper() -> bool: ...


class GH_ResourceGate:
    @property
    def BlackIcon() -> Bitmap: ...
    @property
    def Error_12x12() -> Bitmap: ...
    @property
    def Error_16x16() -> Bitmap: ...
    @property
    def Error_24x24() -> Bitmap: ...
    @property
    def Error_40x40() -> Bitmap: ...
    @property
    def Info_12x12() -> Bitmap: ...
    @property
    def Info_16x16() -> Bitmap: ...
    @property
    def Info_24x24() -> Bitmap: ...
    @property
    def Info_40x40() -> Bitmap: ...
    @property
    def OK_12x12() -> Bitmap: ...
    @property
    def OK_16x16() -> Bitmap: ...
    @property
    def OK_24x24() -> Bitmap: ...
    @property
    def OK_40x40() -> Bitmap: ...
    @property
    def Warning_12x12() -> Bitmap: ...
    @property
    def Warning_16x16() -> Bitmap: ...
    @property
    def Warning_24x24() -> Bitmap: ...
    @property
    def Warning_40x40() -> Bitmap: ...
    @property
    def WhiteIcon() -> Bitmap: ...


class GH_RhinoScriptInterface:
    def __init__(self): ...
    def AssignDataToParameter(self, parameterID: str, data: Object) -> bool: ...
    def BakeDataInObject(self, objectID: str) -> Object: ...
    def CloseAllDocuments(self) -> bool: ...
    def CloseDocument(self) -> bool: ...
    def DisableBanner(self) -> None: ...
    def DisableSolver(self) -> None: ...
    def EnableBanner(self) -> None: ...
    def EnableSolver(self) -> None: ...
    def HideEditor(self) -> None: ...
    def IsEditorLoaded(self) -> bool: ...
    def IsEditorVisible(self) -> bool: ...
    def IsSolverEnabled(self) -> bool: ...
    def LoadEditor(self) -> None: ...
    def OpenDocument(self, filename: str) -> bool: ...
    def RunAsCommand(self, ghDoc: GH_Document, command: Command, rhinoDoc: RhinoDoc, mode: RunMode) -> Result: ...
    def RunHeadless(self) -> None: ...
    def RunSolver(self, expireAllObjects: bool) -> None: ...
    def SaveDocument(self) -> bool: ...
    def SaveDocumentAs(self, filename: str) -> bool: ...
    def SetSliderRangeAndValue(self, sliderID: str, value: float, minimum: float, maximum: float) -> bool: ...
    def SetSliderValue(self, sliderID: str, value: float) -> bool: ...
    def ShowEditor(self) -> None: ...
