__all__ = ['InProcess','InteropWrappers','Notifications','RhinoAccounts']
from typing import Tuple, Set, Iterable, List


class AdvancedSetting:
    UseNewDraftAngleAnalysisUi = 0
    UseCompressionWhenSaving = 1
    TestAdvancedString = 2
    TestAdvancedInt = 3
    PdfOptionalContentGroups = 4
    LeaveFloatingPanelsHiddenOnMac = 5
    DisableFileWatchers = 6
    EnableCheckForUpdates = 7
    LeftJustifyNumericText = 8


class Analytics:
    @overload
    def __init__(self, TrackingID: str, Name: str): ...
    @overload
    def __init__(self, TrackingID: str, Name: str, Platform: str, InstallerId: str, Version: str): ...
    @property
    def AppInstallerId(self) -> str: ...
    @property
    def AppName(self) -> str: ...
    @property
    def AppPlatform(self) -> str: ...
    @property
    def AppVersion(self) -> str: ...
    @property
    def GoogleAnalyticsTrackingID(self) -> str: ...
    @property
    def UsageStatisticsEnabled() -> bool: ...
    @property
    def UserId() -> Guid: ...
    @overload
    def Send(self, data: NameValueCollection) -> None: ...
    @overload
    def Send(self, Category: str) -> None: ...
    @overload
    def Send(self, Category: str, Action: str) -> None: ...
    @overload
    def Send(self, Category: str, Action: str, Label: str) -> None: ...
    @overload
    def Send(self, Category: str, Action: str, Label: str, Value: UInt32) -> None: ...
    @AppInstallerId.setter
    def AppInstallerId(self, value: str) -> None: ...
    @AppName.setter
    def AppName(self, value: str) -> None: ...
    @AppPlatform.setter
    def AppPlatform(self, value: str) -> None: ...
    @AppVersion.setter
    def AppVersion(self, value: str) -> None: ...
    @GoogleAnalyticsTrackingID.setter
    def GoogleAnalyticsTrackingID(self, value: str) -> None: ...


class AssemblyResolver:
    def AddSearchFile(file: str) -> None: ...
    def AddSearchFolder(folder: str) -> None: ...


class CommonObject:
    def Dispose(self) -> None: ...
    def EnsurePrivateCopy(self) -> None: ...
    def FromBase64String(archive3dm: int, opennurbs: int, base64Data: str) -> CommonObject: ...
    def FromJSON(jsonDictionary: Dictionary) -> CommonObject: ...
    @property
    def Disposed(self) -> bool: ...
    @property
    def HasUserData(self) -> bool: ...
    @property
    def IsDocumentControlled(self) -> bool: ...
    @property
    def IsValid(self) -> bool: ...
    @property
    def PerformCorruptionTesting() -> bool: ...
    @property
    def UserData(self) -> UserDataList: ...
    @property
    def UserDictionary(self) -> ArchivableDictionary: ...
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...
    def IsValidWithLog(self) -> Tuple[bool, str]: ...
    @PerformCorruptionTesting.setter
    def PerformCorruptionTesting(value: bool) -> None: ...
    def ToJSON(self, options: SerializationOptions) -> str: ...


class CorruptGeometryException:
    @property
    def CommonObject(self) -> CommonObject: ...
    @property
    def Pointer(self) -> IntPtr: ...


class DocumentCollectedException:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: str): ...


class ExceptionReportDelegate:
    def __init__(self, object: Object, method: IntPtr): ...
    def BeginInvoke(self, source: str, ex: Exception, callback: AsyncCallback, object: Object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, source: str, ex: Exception) -> None: ...


class FillProc:
    def __init__(self, object: Object, method: IntPtr): ...
    def BeginInvoke(self, topl: int, bottoml: int, topr: int, bottomr: int, callback: AsyncCallback, object: Object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, topl: int, bottoml: int, topr: int, bottomr: int) -> None: ...


class HostUtils:
    def add_OnExceptionReport(value: ExceptionReportDelegate) -> None: ...
    def add_OnSendLogMessageToCloud(value: SendLogMessageToCloudDelegate) -> None: ...
    def AutoInstallPlugInFolder(currentUser: bool) -> str: ...
    def CallFromCoreRhino(task: str) -> int: ...
    def CheckForRdk(throwOnFalse: bool, usePreviousResult: bool) -> bool: ...
    def ClearFpuExceptionStatus() -> None: ...
    @overload
    def CreateCommands(plugin: PlugIn) -> None: ...
    @overload
    def CreateCommands(pPlugIn: IntPtr, pluginAssembly: Assembly) -> int: ...
    def CreatePlugIn(pluginType: Type, printDebugMessages: bool) -> PlugIn: ...
    @overload
    def DebugDumpToString(geometry: GeometryBase) -> str: ...
    @overload
    def DebugDumpToString(bezierCurve: BezierCurve) -> str: ...
    @overload
    def DebugString(msg: str) -> None: ...
    @overload
    def DebugString(format: str, args: Set(Object)) -> None: ...
    def DisplayOleAlerts(display: bool) -> None: ...
    @overload
    def ExceptionReport(ex: Exception) -> None: ...
    @overload
    def ExceptionReport(source: str, ex: Exception) -> None: ...
    def ExecuteNamedCallback(name: str, args: NamedParametersEventArgs) -> bool: ...
    def FileNameEndsWithRhinoBackupExtension(fileName: str) -> bool: ...
    def FileNameEndsWithRhinoExtension(fileName: str) -> bool: ...
    @property
    def ComputerSerialNumber() -> str: ...
    @property
    def CurrentOSLanguage() -> UInt32: ...
    @property
    def DeviceId() -> Guid: ...
    @property
    def DeviceName() -> str: ...
    @property
    def OperatingSystemBuildNumber() -> str: ...
    @property
    def OperatingSystemEdition() -> str: ...
    @property
    def OperatingSystemInstallationType() -> str: ...
    @property
    def OperatingSystemProductName() -> str: ...
    @property
    def OperatingSystemVersion() -> str: ...
    @property
    def RunningAsRhinoInside() -> bool: ...
    @property
    def RunningInDarkMode() -> bool: ...
    @property
    def RunningInMono() -> bool: ...
    @property
    def RunningInRhino() -> bool: ...
    @property
    def RunningInWindowsContainer() -> bool: ...
    @property
    def RunningOnOSX() -> bool: ...
    @property
    def RunningOnWindows() -> bool: ...
    @property
    def SendDebugToCommandLine() -> bool: ...
    def GetAbsolutePath(relativePath: str, bRelativePathisFileName: bool, relativeTo: str, bRelativeToIsFileName: bool) -> Tuple[bool, str]: ...
    def GetActivePlugInVersionFolders(currentUser: bool) -> Iterable[DirectoryInfo]: ...
    def GetAssemblySearchPaths() -> Set(str): ...
    def GetCurrentProcessInfo() -> Tuple[str, Version]: ...
    def GetCustomComputeEndpoints() -> Set(Tuple): ...
    def GetPlatformService(assemblyPath: str, typeFullName: str) -> T: ...
    def GetRhinoDotNetAssembly() -> Assembly: ...
    def InitializeRhinoCommon() -> None: ...
    def InitializeRhinoCommon_RDK() -> None: ...
    def InitializeZooClient() -> None: ...
    def InPlaceConstCast(geometry: GeometryBase, makeNonConst: bool) -> None: ...
    def IsManagedDll(path: str) -> bool: ...
    def IsRhinoBackupFileExtension(fileExtension: str) -> bool: ...
    def IsRhinoFileExtension(fileExtension: str) -> bool: ...
    def RecordInitInstanceTime(description: str) -> None: ...
    def RegisterComputeEndpoint(endpointPath: str, t: Type) -> None: ...
    def RegisterDynamicCommand(plugin: PlugIn, cmd: Command) -> bool: ...
    def RegisterNamedCallback(name: str, callback: EventHandler) -> None: ...
    def remove_OnExceptionReport(value: ExceptionReportDelegate) -> None: ...
    def remove_OnSendLogMessageToCloud(value: SendLogMessageToCloudDelegate) -> None: ...
    def RhinoCommonExceptionHandler(title: str, sender: Object, ex: Exception) -> None: ...
    def SendLogMessageToCloudCallbackProc(msg_type: LogMessageType, pwStringClass: IntPtr, pwStringDesc: IntPtr, pwStringMessage: IntPtr) -> None: ...
    @SendDebugToCommandLine.setter
    def SendDebugToCommandLine(value: bool) -> None: ...
    def SetInShutDown() -> None: ...
    def ShutDownRhinoCommon_RDK() -> None: ...
    def UnhandledThreadException(sender: Object, e: ThreadExceptionEventArgs) -> None: ...


class ImportOptionsSections:
    AdvancedDisplay = 0
    Alias = 1
    Appearance = 2
    ChooseOneObject = 3
    ControlPointContextMenu = 4
    CursorToolTip = 5
    Display = 6
    File = 7
    General = 8
    Grid = 9
    ModelAid = 10
    Mouse = 11
    NeverRepeatCommands = 12
    ObjectContextMenu = 13
    SearchPath = 14
    ShortcutKey = 15
    Smarttrack = 16
    View = 17
    ViewportContextMenu = 18
    ToolPaletteSettings = 19
    Count = 20


class InstanceAttributeField:
    def __init__(self, key: str, prompt: str, defaultValue: str): ...
    @property
    def DefaultValue(self) -> str: ...
    @property
    def Key(self) -> str: ...
    @property
    def Prompt(self) -> str: ...


class Interop:
    def CreateFromNativePointer(pGeometry: IntPtr) -> GeometryBase: ...
    def FileReadOptionsConstPointer(options: FileReadOptions) -> IntPtr: ...
    def FileWriteOptionsConstPointer(options: FileWriteOptions) -> IntPtr: ...
    def FontFromPointer(ptrManagedFont: IntPtr) -> Font: ...
    def FromOnBrep(source: Object) -> Brep: ...
    def FromOnCurve(source: Object) -> Curve: ...
    def FromOnMesh(source: Object) -> Mesh: ...
    def FromOnSurface(source: Object) -> Surface: ...
    def NativeGeometryConstPointer(geometry: GeometryBase) -> IntPtr: ...
    def NativeGeometryNonConstPointer(geometry: GeometryBase) -> IntPtr: ...
    @overload
    def NativeNonConstPointer(settings: ViewCaptureSettings) -> IntPtr: ...
    @overload
    def NativeNonConstPointer(pipeline: DisplayPipeline) -> IntPtr: ...
    @overload
    def NativeNonConstPointer(getPoint: GetPoint) -> IntPtr: ...
    @overload
    def NativeNonConstPointer(viewport: RhinoViewport) -> IntPtr: ...
    @overload
    def NativeNonConstPointer(viewport: ViewportInfo) -> IntPtr: ...
    def NativeRhinoDocPointer(doc: RhinoDoc) -> IntPtr: ...
    @overload
    def NSFontFromFont(font: Font) -> IntPtr: ...
    @overload
    def NSFontFromFont(font: Font, pointSize: float) -> IntPtr: ...
    def PlugInPointer(plugin: PlugIn) -> IntPtr: ...
    def RhinoObjectConstPointer(rhinoObject: RhinoObject) -> IntPtr: ...
    def RhinoObjectFromPointer(pRhinoObject: IntPtr) -> RhinoObject: ...
    def ToIRhinoViewport(source: RhinoViewport) -> Object: ...
    def ToOnBrep(source: Brep) -> Object: ...
    def ToOnCurve(source: Curve) -> Object: ...
    def ToOnMesh(source: Mesh) -> Object: ...
    def ToOnSurface(source: Surface) -> Object: ...
    def ToOnXform(source: Transform) -> Object: ...
    def TryCopyFromOnArc(source: Object) -> Tuple[bool, Arc]: ...
    def TryCopyToOnArc(source: Arc, destination: Object) -> bool: ...
    def ViewCaptureFromPointer(ptrViewCapture: IntPtr) -> ViewCaptureSettings: ...


class IPlatformServiceLocator:
    def GetService(self) -> T: ...


class IZooClientUtilities:
    def AskUserForLicense(self, verify: Object, parameters: ZooClientParameters) -> bool: ...
    def CheckInLicense(self, verify: Object, productId: Guid) -> bool: ...
    def CheckOutLicense(self, verify: Object, productId: Guid) -> bool: ...
    def ConvertLicense(self, verify: Object, productId: Guid) -> bool: ...
    def DeleteLicense(self, verify: Object, productId: Guid) -> bool: ...
    def Echo(self, verify: Object, message: str) -> str: ...
    @property
    def LoggedInUserAvatar(self) -> Image: ...
    @property
    def LoggedInUserName(self) -> str: ...
    @property
    def UserIsLoggedIn(self) -> bool: ...
    def GetCurrentTime(self) -> DateTime: ...
    def GetLicense(self, verify: Object, parameters: ZooClientParameters) -> bool: ...
    def GetLicenseStatus(self, verify: Object) -> Set(LicenseStatus): ...
    def GetLicenseType(self, verify: Object, productId: Guid) -> int: ...
    def GetOneLicenseStatus(self, verify: Object, productId: Guid) -> LicenseStatus: ...
    def GetRegisteredOwnerInfo(self, verify: Object, productId: Guid, registeredOwner: str, registeredOrganization: str) -> Tuple[bool, str, str]: ...
    def Initialize(self, verify: Object) -> bool: ...
    def IsCheckOutEnabled(self, verify: Object) -> bool: ...
    def LicenseOptionsHandler(self, verify: Object, parameters: ZooClientParameters) -> bool: ...
    def LoginToCloudZoo(self) -> bool: ...
    def LogoutOfCloudZoo(self) -> bool: ...
    @overload
    def ReturnLicense(self, verify: Object, productId: Guid) -> bool: ...
    @overload
    def ReturnLicense(self, verify: Object, productPath: str, productId: Guid) -> bool: ...
    def ShowBuyLicenseUi(self, verify: Object, productId: Guid) -> None: ...
    def ShowLicenseValidationUi(self, verify: Object, cdkey: str) -> bool: ...
    def ShowRhinoExpiredMessage(self, mode: Mode, result: int) -> Tuple[bool, int]: ...


class LicenseStateChangedEventArgs:
    def __init__(self, callingRhinoCommonAllowed: bool): ...
    @property
    def CallingRhinoCommonAllowed(self) -> bool: ...


class LicenseTypes:
    Undefined = 0
    Standalone = 1
    ZooAutoDetect = 2
    ZooManualDetect = 3
    CloudZoo = 4


class LogMessageType:
    unknown = 0
    information = 1
    warning = 2
    error = 3
    assert = 4


class Mode:
    NormalMode = 0
    ViewerMode = 1
    BetaMode = 2
    InvalidMode = 100


class NamedParametersEventArgs:
    def __init__(self): ...
    def Dispose(self) -> None: ...
    @overload
    def Set(self, name: str, values: Iterable[GeometryBase]) -> None: ...
    @overload
    def Set(self, name: str, value: GeometryBase) -> None: ...
    @overload
    def Set(self, name: str, value: Color) -> None: ...
    @overload
    def Set(self, name: str, value: Vector3d) -> None: ...
    @overload
    def Set(self, name: str, value: float) -> None: ...
    @overload
    def Set(self, name: str, value: UInt32) -> None: ...
    @overload
    def Set(self, name: str, value: Point3d) -> None: ...
    @overload
    def Set(self, name: str, strings: Iterable[str]) -> None: ...
    @overload
    def Set(self, name: str, value: int) -> None: ...
    @overload
    def Set(self, name: str, value: str) -> None: ...
    @overload
    def Set(self, name: str, value: bool) -> None: ...
    def SetWindowHandle(self, name: str, value: IntPtr) -> None: ...
    def TryGetBool(self, name: str) -> Tuple[bool, bool]: ...
    def TryGetColor(self, name: str) -> Tuple[bool, Color]: ...
    def TryGetDouble(self, name: str) -> Tuple[bool, float]: ...
    def TryGetGeometry(self, name: str) -> Tuple[bool, Set(GeometryBase)]: ...
    def TryGetInt(self, name: str) -> Tuple[bool, int]: ...
    def TryGetPoint(self, name: str) -> Tuple[bool, Point3d]: ...
    def TryGetRhinoObjects(self, key: str) -> Tuple[bool, Set(RhinoObject)]: ...
    def TryGetString(self, name: str) -> Tuple[bool, str]: ...
    def TryGetStrings(self, name: str) -> Tuple[bool, Set(str)]: ...
    def TryGetUnsignedInt(self, name: str) -> Tuple[bool, UInt32]: ...
    def TryGetVector(self, name: str) -> Tuple[bool, Vector3d]: ...
    def TryGetViewport(self, name: str) -> Tuple[bool, ViewportInfo]: ...
    def TryGetWindowHandle(self, name: str) -> Tuple[bool, IntPtr]: ...


class NotLicensedException:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, message: str, inner: Exception): ...


class PathPoint:
    @property
    def Location(self) -> PointF: ...
    @property
    def PointType(self) -> PointType: ...
    @Location.setter
    def Location(self, value: PointF) -> None: ...
    @PointType.setter
    def PointType(self, value: PointType) -> None: ...


class Pen:
    def __init__(self): ...
    @property
    def Color(self) -> Color: ...
    @property
    def Width(self) -> Single: ...


class PointType:
    Move = 0
    Line = 1
    CubicBezier = 2
    Close = 3


class PythonCompiledCode:
    def Execute(self, scope: PythonScript) -> None: ...


class PythonScript:
    def AddRuntimeAssembly(assembly: Assembly) -> None: ...
    def Compile(self, script: str) -> PythonCompiledCode: ...
    def ContainsVariable(self, name: str) -> bool: ...
    def Create() -> PythonScript: ...
    def CreateTextEditorControl(self, script: str, helpcallback: Action) -> Object: ...
    def EvaluateExpression(self, statements: str, expression: str) -> Object: ...
    def ExecuteFile(self, path: str) -> bool: ...
    def ExecuteFileInScope(self, path: str) -> bool: ...
    def ExecuteScript(self, script: str) -> bool: ...
    @property
    def ContextId(self) -> int: ...
    @property
    def Output(self) -> Action: ...
    @property
    def ScriptContextCommand(self) -> Command: ...
    @property
    def ScriptContextDoc(self) -> Object: ...
    @property
    def SearchPaths() -> Set(str): ...
    def GetStackTraceFromException(self, ex: Exception) -> str: ...
    def GetVariable(self, name: str) -> Object: ...
    def GetVariableNames(self) -> Iterable[str]: ...
    def RemoveVariable(self, name: str) -> None: ...
    def RuntimeAssemblies() -> Set(Assembly): ...
    @ContextId.setter
    def ContextId(self, value: int) -> None: ...
    @Output.setter
    def Output(self, value: Action) -> None: ...
    @ScriptContextCommand.setter
    def ScriptContextCommand(self, value: Command) -> None: ...
    @ScriptContextDoc.setter
    def ScriptContextDoc(self, value: Object) -> None: ...
    @SearchPaths.setter
    def SearchPaths(value: Set(str)) -> None: ...
    def SetIntellisenseVariable(self, name: str, value: Object) -> None: ...
    def SetupScriptContext(self, doc: Object) -> None: ...
    def SetVariable(self, name: str, value: Object) -> None: ...


class RdkNotLoadedException:
    def __init__(self): ...


class RiskyAction:
    def __init__(self, description: str, file: str, member: str, line: int): ...
    def Dispose(self) -> None: ...


class SendLogMessageToCloudDelegate:
    def __init__(self, object: Object, method: IntPtr): ...
    def BeginInvoke(self, msg_type: LogMessageType, sClass: str, sDesc: str, sMessage: str, callback: AsyncCallback, object: Object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, msg_type: LogMessageType, sClass: str, sDesc: str, sMessage: str) -> None: ...


class SetClipRectProc:
    def __init__(self, object: Object, method: IntPtr): ...
    def BeginInvoke(self, left: int, top: int, right: int, bottom: int, callback: AsyncCallback, object: Object) -> Tuple[IAsyncResult, int, int, int, int]: ...
    def EndInvoke(self, left: int, top: int, right: int, bottom: int, result: IAsyncResult) -> Tuple[int, int, int, int]: ...
    def Invoke(self, left: int, top: int, right: int, bottom: int) -> Tuple[int, int, int, int]: ...


class Skin:
    @property
    def ActiveSkin() -> Skin: ...
    @property
    def Settings(self) -> PersistentSettings: ...


class TextFields:
    @overload
    def Area(id: str) -> float: ...
    @overload
    def Area(id: str, unitSystem: str) -> float: ...
    def BlockAttributeText(key: str, prompt: str, defaultValue: str) -> str: ...
    def BlockInstanceCount(instanceDefinitionNameOrId: str) -> int: ...
    def BlockInstanceName(blockId: str) -> str: ...
    @overload
    def CurveLength(id: str) -> float: ...
    @overload
    def CurveLength(id: str, unitSystem: str) -> float: ...
    @overload
    def Date() -> str: ...
    @overload
    def Date(dateFormat: str) -> str: ...
    @overload
    def Date(dateFormat: str, languageId: str) -> str: ...
    @overload
    def DateModified() -> str: ...
    @overload
    def DateModified(dateFormat: str) -> str: ...
    @overload
    def DateModified(dateFormat: str, languageId: str) -> str: ...
    def DetailScale(detailId: str, scaleFormat: str) -> str: ...
    def DocumentText(key: str) -> str: ...
    @overload
    def FileName() -> str: ...
    @overload
    def FileName(options: str) -> str: ...
    @overload
    def GetInstanceAttributeFields(str: str) -> Set(InstanceAttributeField): ...
    @overload
    def GetInstanceAttributeFields(idef: InstanceDefinition) -> Set(InstanceAttributeField): ...
    @overload
    def GetInstanceAttributeFields(text: TextObject) -> Set(InstanceAttributeField): ...
    def LayerName(layerId: str) -> str: ...
    @overload
    def LayoutUserText(key: str) -> str: ...
    @overload
    def LayoutUserText(layoutId: str, key: str) -> str: ...
    def ModelUnits() -> str: ...
    def Notes() -> str: ...
    def NumPages() -> int: ...
    def ObjectLayer(id: str) -> str: ...
    def ObjectName(id: str) -> str: ...
    def PageHeight() -> float: ...
    @overload
    def PageName() -> str: ...
    @overload
    def PageName(id: str) -> str: ...
    def PageNumber() -> int: ...
    def PageWidth() -> float: ...
    def PaperName() -> str: ...
    def PointCoordinate(pointId: str, axis: str) -> str: ...
    @overload
    def UserText(id: str, key: str) -> str: ...
    @overload
    def UserText(id: str, key: str, prompt: str) -> str: ...
    @overload
    def UserText(id: str, key: str, prompt: str, defaultValue: str) -> str: ...
    @overload
    def Volume(id: str) -> float: ...
    @overload
    def Volume(id: str, unitSystem: str) -> float: ...


class VectorArcProc:
    def __init__(self, object: Object, method: IntPtr): ...
    def BeginInvoke(self, argb: int, thickness: Single, dashed: int, arc: Arc, callback: AsyncCallback, object: Object) -> Tuple[IAsyncResult, Arc]: ...
    def EndInvoke(self, arc: Arc, result: IAsyncResult) -> Tuple[Arc]: ...
    def Invoke(self, argb: int, thickness: Single, dashed: int, arc: Arc) -> Tuple[Arc]: ...


class VectorBitmapProc:
    def __init__(self, object: Object, method: IntPtr): ...
    def BeginInvoke(self, hBmp: IntPtr, m11: float, m12: float, m21: float, m22: float, dx: float, dy: float, callback: AsyncCallback, object: Object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, hBmp: IntPtr, m11: float, m12: float, m21: float, m22: float, dx: float, dy: float) -> None: ...


class VectorClipPathProc:
    def __init__(self, object: Object, method: IntPtr): ...
    def BeginInvoke(self, count: int, points: IntPtr, asBeziers: int, callback: AsyncCallback, object: Object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, count: int, points: IntPtr, asBeziers: int) -> None: ...


class VectorFillPolygonProc:
    def __init__(self, object: Object, method: IntPtr): ...
    def BeginInvoke(self, argb: int, count: int, points: IntPtr, callback: AsyncCallback, object: Object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, argb: int, count: int, points: IntPtr) -> None: ...


class VectorGradientProc:
    def __init__(self, object: Object, method: IntPtr): ...
    def BeginInvoke(self, pEngine: IntPtr, pHatch: IntPtr, strokeWidth: Single, pHatchPattern: IntPtr, gradientCount: int, colors: IntPtr, stops: IntPtr, points: IntPtr, linearGradient: int, boundaryColor: int, callback: AsyncCallback, object: Object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, pEngine: IntPtr, pHatch: IntPtr, strokeWidth: Single, pHatchPattern: IntPtr, gradientCount: int, colors: IntPtr, stops: IntPtr, points: IntPtr, linearGradient: int, boundaryColor: int) -> None: ...


class VectorPathProc:
    def __init__(self, object: Object, method: IntPtr): ...
    def BeginInvoke(self, begin: int, argb: int, callback: AsyncCallback, object: Object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, begin: int, argb: int) -> None: ...


class VectorPointProc:
    def __init__(self, object: Object, method: IntPtr): ...
    def BeginInvoke(self, style: int, screenX: Single, screenY: Single, fillArgb: int, strokeArgb: int, diameterPixels: Single, innerDiameterPixels: Single, strokeWidthPixels: Single, rotationRadians: Single, callback: AsyncCallback, object: Object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, style: int, screenX: Single, screenY: Single, fillArgb: int, strokeArgb: int, diameterPixels: Single, innerDiameterPixels: Single, strokeWidthPixels: Single, rotationRadians: Single) -> None: ...


class VectorPolylineProc:
    def __init__(self, object: Object, method: IntPtr): ...
    def BeginInvoke(self, argb: int, thickness: Single, dashed: int, count: int, points: IntPtr, callback: AsyncCallback, object: Object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, argb: int, thickness: Single, dashed: int, count: int, points: IntPtr) -> None: ...


class VectorRoundedRectProc:
    def __init__(self, object: Object, method: IntPtr): ...
    def BeginInvoke(self, centerX: Single, centerY: Single, pixelWidth: Single, pixelHeight: Single, cornerRadius: Single, strokeColor: int, strokeWidth: Single, fillColor: int, callback: AsyncCallback, object: Object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, centerX: Single, centerY: Single, pixelWidth: Single, pixelHeight: Single, cornerRadius: Single, strokeColor: int, strokeWidth: Single, fillColor: int) -> None: ...


class VectorStringProc:
    def __init__(self, object: Object, method: IntPtr): ...
    def BeginInvoke(self, constPtrString: IntPtr, argbTextColor: int, x: float, y: float, angle: Single, alignment: int, heightPixels: Single, constPtrFont: IntPtr, callback: AsyncCallback, object: Object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, constPtrString: IntPtr, argbTextColor: int, x: float, y: float, angle: Single, alignment: int, heightPixels: Single, constPtrFont: IntPtr) -> None: ...


class ViewCaptureWriter:
    def __init__(self, dpi: float, pageSize: Size): ...
    def Draw(self, constPtrPrintInfo: IntPtr, doc: RhinoDoc) -> None: ...


class ZooClientParameters:
    def __init__(self, productGuid: Guid, licenseGuid: Guid, productTitle: str, productBuildType: int, capabilities: LicenseCapabilities, licenseEntryTextMask: str, productPath: str, parentWindow: Object, selectedLicenseType: LicenseTypes, validateProductKey: ValidateProductKeyDelegate, onLeaseChangedDelegate: OnLeaseChangedDelegate, verifyLicenseKeyDelegate: VerifyLicenseKeyDelegate, verifyPreviousVersionLicenseKeyDelegate: VerifyPreviousVersionLicenseDelegate): ...
    @property
    def Capabilities(self) -> LicenseCapabilities: ...
    @property
    def LicenseEntryTextMask(self) -> str: ...
    @property
    def LicenseGuid(self) -> Guid: ...
    @property
    def OnLeaseChanged(self) -> OnLeaseChangedDelegate: ...
    @property
    def ParentWindow(self) -> Object: ...
    @property
    def ProductBuildType(self) -> int: ...
    @property
    def ProductGuid(self) -> Guid: ...
    @property
    def ProductPath(self) -> str: ...
    @property
    def ProductTitle(self) -> str: ...
    @property
    def SelectedLicenseType(self) -> LicenseTypes: ...
    @Capabilities.setter
    def Capabilities(self, value: LicenseCapabilities) -> None: ...
    @SelectedLicenseType.setter
    def SelectedLicenseType(self, value: LicenseTypes) -> None: ...
    def VerifyLicenseKey(self, licenseKey: str, validationCode: str, validationCodeInstallDate: DateTime, gracePeriodExpired: bool) -> Tuple[ValidateResult, LicenseData]: ...
    def VerifyPreviousVersionLicense(self, license: str, previousVersionLicense: str) -> Tuple[bool, str]: ...
