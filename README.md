# Suzuki_analyze2
簡単な日本株の分析ツールです

#　作者
名前：Taichi Suzuki

Translated Report (Full Report Below)
-------------------------------------

Process:               Python [20761]
Path:                  /Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python
Identifier:            com.apple.python3
Version:               3.9.6 (3.9.6)
Build Info:            python3-141000000000000~2624
Code Type:             X86-64 (Native)
Parent Process:        zsh [20654]
Responsible:           Code [18307]
User ID:               501

Date/Time:             2026-08-16 15:12:17.6723 +0900
OS Version:            macOS 14.8.9 (23J631)
Report Version:        12
Anonymous UUID:        5151B66A-5A88-D619-1456-DABBB786D2D6

Sleep/Wake UUID:       A72ACAAA-C6AF-4DA3-82A4-AFE3D3E1EAF9

Time Awake Since Boot: 100000 seconds
Time Since Wake:       1287 seconds

System Integrity Protection: enabled

Crashed Thread:        0  Dispatch queue: com.apple.main-thread

Exception Type:        EXC_CRASH (SIGABRT)
Exception Codes:       0x0000000000000000, 0x0000000000000000

Termination Reason:    Namespace SIGNAL, Code 6 Abort trap: 6
Terminating Process:   Python [20761]

Application Specific Information:
abort() called


Thread 0 Crashed::  Dispatch queue: com.apple.main-thread
0   libsystem_kernel.dylib        	    0x7ff816570dd6 __pthread_kill + 10
1   libsystem_pthread.dylib       	    0x7ff8165a9e51 pthread_kill + 262
2   libsystem_c.dylib             	    0x7ff8164cfa59 abort + 126
3   Tcl                           	    0x7ffb1f7097ee Tcl_PanicVA + 364
4   Tcl                           	    0x7ffb1f70986e Tcl_Panic + 128
5   Tk                            	    0x7ffb1f89b36c TkpInit + 552
6   Tk                            	    0x7ffb1f81c3bd 0x7ffb1f7ee000 + 189373
7   _tkinter.cpython-39-darwin.so 	       0x10883d66e 0x108835000 + 34414
8   _tkinter.cpython-39-darwin.so 	       0x1088380b3 0x108835000 + 12467
9   _tkinter.cpython-39-darwin.so 	       0x1088379d3 0x108835000 + 10707
10  Python3                       	       0x10914f337 0x1090cd000 + 533303
11  Python3                       	       0x1091ec77b 0x1090cd000 + 1177467
12  Python3                       	       0x1091e9557 _PyEval_EvalFrameDefault + 23527
13  Python3                       	       0x1091ed693 0x1090cd000 + 1181331
14  Python3                       	       0x10910ff55 _PyFunction_Vectorcall + 261
15  Python3                       	       0x10910f652 _PyObject_FastCallDictTstate + 258
16  Python3                       	       0x10911033a _PyObject_Call_Prepend + 154
17  Python3                       	       0x10916e880 0x1090cd000 + 661632
18  Python3                       	       0x109166b74 0x1090cd000 + 629620
19  Python3                       	       0x10910f830 _PyObject_MakeTpCall + 384
20  Python3                       	       0x1091ec850 0x1090cd000 + 1177680
21  Python3                       	       0x1091e9557 _PyEval_EvalFrameDefault + 23527
22  Python3                       	       0x109110050 0x1090cd000 + 274512
23  Python3                       	       0x1091ec77b 0x1090cd000 + 1177467
24  Python3                       	       0x1091e95eb _PyEval_EvalFrameDefault + 23675
25  Python3                       	       0x1091ed693 0x1090cd000 + 1181331
26  Python3                       	       0x1091e3871 PyEval_EvalCode + 81
27  Python3                       	       0x10922aea1 0x1090cd000 + 1433249
28  Python3                       	       0x10922b013 0x1090cd000 + 1433619
29  Python3                       	       0x1092292a4 PyRun_SimpleFileExFlags + 708
30  Python3                       	       0x1092466f0 Py_RunMain + 1840
31  Python3                       	       0x109246b80 0x1090cd000 + 1547136
32  Python3                       	       0x109246bdb Py_BytesMain + 43
33  dyld                          	    0x7ff81621e345 start + 1909

Thread 1:
0   libsystem_pthread.dylib       	    0x7ff8165a5aa0 start_wqthread + 0

Thread 2:
0   libsystem_pthread.dylib       	    0x7ff8165a5aa0 start_wqthread + 0

Thread 3:
0   libsystem_pthread.dylib       	    0x7ff8165a5aa0 start_wqthread + 0


Thread 0 crashed with X86 Thread State (64-bit):
  rax: 0x0000000000000000  rbx: 0x0000000000000006  rcx: 0x00007ff7b7913538  rdx: 0x0000000000000000
  rdi: 0x0000000000000103  rsi: 0x0000000000000006  rbp: 0x00007ff7b7913560  rsp: 0x00007ff7b7913538
   r8: 0x00007ff859af2250   r9: 0x00000000ffffff00  r10: 0x0000000000000000  r11: 0x0000000000000246
  r12: 0x0000000000000103  r13: 0x00007fd63f8922d0  r14: 0x00007ff859aeaa80  r15: 0x0000000000000016
  rip: 0x00007ff816570dd6  rfl: 0x0000000000000246  cr2: 0x0000000000000000
  
Logical CPU:     0
Error Code:      0x02000148 
Trap Number:     133


Binary Images:
       0x108a0e000 -        0x108a18fff math.cpython-39-darwin.so (*) <ae45d155-94e0-310e-94ce-1c2757018276> /Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/lib-dynload/math.cpython-39-darwin.so
       0x108989000 -        0x10898efff select.cpython-39-darwin.so (*) <1bc366c2-bae5-397d-8114-abb2e23292bf> /Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/lib-dynload/select.cpython-39-darwin.so
       0x1089b8000 -        0x1089bbfff _posixsubprocess.cpython-39-darwin.so (*) <3bdb23d1-a50b-3d9e-a5c5-78f3c47cb6e5> /Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/lib-dynload/_posixsubprocess.cpython-39-darwin.so
       0x1089ab000 -        0x1089adfff grp.cpython-39-darwin.so (*) <78706dc5-d30c-3b28-8a69-9742b3a794c1> /Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/lib-dynload/grp.cpython-39-darwin.so
       0x108801000 -        0x108804fff _heapq.cpython-39-darwin.so (*) <8e398855-3ad0-3316-b757-e6d055a773bc> /Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/lib-dynload/_heapq.cpython-39-darwin.so
       0x108835000 -        0x10883efff _tkinter.cpython-39-darwin.so (*) <78acc5ac-f6ff-3d92-b5f5-4d6ff805f14a> /Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/lib-dynload/_tkinter.cpython-39-darwin.so
       0x10880f000 -        0x108812fff com.apple.IO80211 (1.0) <822d5166-e0bd-394e-852c-50e775fe7277> /System/Library/PrivateFrameworks/IO80211.framework/Versions/A/IO80211
       0x1093b2000 -        0x109405fff IO80211Old.dylib (*) <d5ce0007-6e6e-383c-abe9-d66eb450ae2d> /System/Library/PrivateFrameworks/IO80211.framework/Versions/A/IO80211Old.dylib
       0x1090cd000 -        0x10932cfff com.apple.python3 (3.9.6) <f8a6eb86-164c-36f7-97f2-8f6fadae8459> /Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Python3
       0x1085ea000 -        0x1085ebfff com.apple.python3 (3.9.6) <c22a284e-5ae7-3332-95f5-de456ff5188e> /Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python
    0x7ff816569000 -     0x7ff8165a3ff7 libsystem_kernel.dylib (*) <9419d8b3-682e-37c0-ace9-6125e601c289> /usr/lib/system/libsystem_kernel.dylib
    0x7ff8165a4000 -     0x7ff8165affff libsystem_pthread.dylib (*) <b299628a-6884-321f-b99a-46eaaa427093> /usr/lib/system/libsystem_pthread.dylib
    0x7ff816450000 -     0x7ff8164d7fff libsystem_c.dylib (*) <163b6214-c567-3d92-99e4-b85415fb81e2> /usr/lib/system/libsystem_c.dylib
    0x7ffb1f68f000 -     0x7ffb1f757fff com.tcltk.tcllibrary (8.5.9) <89dfaddc-609e-36f2-af81-be2d7ab2d1ec> /System/Library/Frameworks/Tcl.framework/Versions/8.5/Tcl
    0x7ffb1f7ee000 -     0x7ffb1f8d0ffe com.tcltk.tklibrary (8.5.9) <faf894b5-455e-38d0-8ed0-340a1b17e4e3> /System/Library/Frameworks/Tk.framework/Versions/8.5/Tk
    0x7ff816218000 -     0x7ff8162a8a87 dyld (*) <14683982-4227-335b-bc68-561d947a8f73> /usr/lib/dyld
               0x0 - 0xffffffffffffffff ??? (*) <00000000-0000-0000-0000-000000000000> ???

External Modification Summary:
  Calls made by other processes targeting this process:
    task_for_pid: 0
    thread_create: 0
    thread_set_state: 0
  Calls made by this process:
    task_for_pid: 0
    thread_create: 0
    thread_set_state: 0
  Calls made by all processes on this machine:
    task_for_pid: 0
    thread_create: 0
    thread_set_state: 0

VM Region Summary:
ReadOnly portion of Libraries: Total=435.3M resident=0K(0%) swapped_out_or_unallocated=435.3M(100%)
Writable regions: Total=1.8G written=0K(0%) resident=0K(0%) swapped_out=0K(0%) unallocated=1.8G(100%)

                                VIRTUAL   REGION 
REGION TYPE                        SIZE    COUNT (non-coalesced) 
===========                     =======  ======= 
Activity Tracing                   256K        1 
ColorSync                          156K       22 
CoreServices                       148K        1 
Dispatch continuations            32.0M        1 
Kernel Alloc Once                    8K        1 
MALLOC                            38.0M       24 
MALLOC guard page                   32K        8 
MALLOC_LARGE (reserved)            384K        1         reserved VM address space (unallocated)
STACK GUARD                         16K        4 
Stack                             17.5M        4 
VM_ALLOCATE                       3336K       15 
VM_ALLOCATE (reserved)             1.7G        2         reserved VM address space (unallocated)
__DATA                            16.7M      319 
__DATA_CONST                      15.2M      208 
__DATA_DIRTY                       641K      103 
__FONT_DATA                        2352        1 
__LINKEDIT                       180.7M       12 
__OBJC_RO                         71.9M        1 
__OBJC_RW                         2201K        2 
__TEXT                           254.6M      339 
mapped file                       53.5M        7 
shared memory                     1296K       18 
===========                     =======  ======= 
TOTAL                              2.4G     1094 
TOTAL, minus reserved VM space   688.0M     1094 



-----------
Full Report
-----------

{"app_name":"Python","timestamp":"2026-08-16 15:12:18.00 +0900","app_version":"3.9.6","slice_uuid":"c22a284e-5ae7-3332-95f5-de456ff5188e","build_version":"3.9.6","platform":1,"bundleID":"com.apple.python3","share_with_app_devs":0,"is_first_party":0,"bug_type":"309","os_version":"macOS 14.8.9 (23J631)","roots_installed":0,"name":"Python","incident_id":"24E31355-6029-469C-B6DC-14A3E437698A"}
{
  "uptime" : 100000,
  "procRole" : "Background",
  "version" : 2,
  "userID" : 501,
  "deployVersion" : 210,
  "modelCode" : "MacBookPro12,1",
  "coalitionID" : 10176,
  "osVersion" : {
    "train" : "macOS 14.8.9",
    "build" : "23J631",
    "releaseType" : "User"
  },
  "captureTime" : "2026-08-16 15:12:17.6723 +0900",
  "codeSigningMonitor" : 0,
  "incident" : "24E31355-6029-469C-B6DC-14A3E437698A",
  "pid" : 20761,
  "cpuType" : "X86-64",
  "roots_installed" : 0,
  "bug_type" : "309",
  "procLaunch" : "2026-08-16 15:12:17.3720 +0900",
  "procStartAbsTime" : 101189726732846,
  "procExitAbsTime" : 101190026418034,
  "procName" : "Python",
  "procPath" : "\/Library\/Developer\/CommandLineTools\/Library\/Frameworks\/Python3.framework\/Versions\/3.9\/Resources\/Python.app\/Contents\/MacOS\/Python",
  "bundleInfo" : {"CFBundleShortVersionString":"3.9.6","CFBundleVersion":"3.9.6","CFBundleIdentifier":"com.apple.python3"},
  "buildInfo" : {"ProjectName":"python3","SourceVersion":"141000000000000","BuildVersion":"2624"},
  "storeInfo" : {"deviceIdentifierForVendor":"4C6DCD1C-1C89-59DA-B49D-85C28DE51E15","thirdParty":true},
  "parentProc" : "zsh",
  "parentPid" : 20654,
  "coalitionName" : "com.microsoft.VSCode",
  "crashReporterKey" : "5151B66A-5A88-D619-1456-DABBB786D2D6",
  "responsiblePid" : 18307,
  "responsibleProc" : "Code",
  "codeSigningID" : "com.apple.python3",
  "codeSigningTeamID" : "",
  "codeSigningFlags" : 570442241,
  "codeSigningValidationCategory" : 1,
  "codeSigningTrustLevel" : 4294967295,
  "wakeTime" : 1287,
  "sleepWakeUUID" : "A72ACAAA-C6AF-4DA3-82A4-AFE3D3E1EAF9",
  "sip" : "enabled",
  "exception" : {"codes":"0x0000000000000000, 0x0000000000000000","rawCodes":[0,0],"type":"EXC_CRASH","signal":"SIGABRT"},
  "termination" : {"flags":0,"code":6,"namespace":"SIGNAL","indicator":"Abort trap: 6","byProc":"Python","byPid":20761},
  "asi" : {"libsystem_c.dylib":["abort() called"]},
  "extMods" : {"caller":{"thread_create":0,"thread_set_state":0,"task_for_pid":0},"system":{"thread_create":0,"thread_set_state":0,"task_for_pid":0},"targeted":{"thread_create":0,"thread_set_state":0,"task_for_pid":0},"warnings":0},
  "faultingThread" : 0,
  "threads" : [{"triggered":true,"id":684436,"threadState":{"r13":{"value":140558165680848},"rax":{"value":0},"rflags":{"value":582},"cpu":{"value":0},"r14":{"value":140704633236096,"symbolLocation":0,"symbol":"_main_thread"},"rsi":{"value":6},"r8":{"value":140704633266768,"symbolLocation":448,"symbol":"__sFX"},"cr2":{"value":0},"rdx":{"value":0},"r10":{"value":0},"r9":{"value":4294967040},"r15":{"value":22},"rbx":{"value":6},"trap":{"value":133},"err":{"value":33554760},"r11":{"value":582},"rip":{"value":140703503420886,"matchesCrashFrame":1},"rbp":{"value":140701913396576},"rsp":{"value":140701913396536},"r12":{"value":259},"rcx":{"value":140701913396536},"flavor":"x86_THREAD_STATE","rdi":{"value":259}},"queue":"com.apple.main-thread","frames":[{"imageOffset":32214,"symbol":"__pthread_kill","symbolLocation":10,"imageIndex":10},{"imageOffset":24145,"symbol":"pthread_kill","symbolLocation":262,"imageIndex":11},{"imageOffset":522841,"symbol":"abort","symbolLocation":126,"imageIndex":12},{"imageOffset":501742,"symbol":"Tcl_PanicVA","symbolLocation":364,"imageIndex":13},{"imageOffset":501870,"symbol":"Tcl_Panic","symbolLocation":128,"imageIndex":13},{"imageOffset":709484,"symbol":"TkpInit","symbolLocation":552,"imageIndex":14},{"imageOffset":189373,"imageIndex":14},{"imageOffset":34414,"imageIndex":5},{"imageOffset":12467,"imageIndex":5},{"imageOffset":10707,"imageIndex":5},{"imageOffset":533303,"imageIndex":8},{"imageOffset":1177467,"imageIndex":8},{"imageOffset":1164631,"symbol":"_PyEval_EvalFrameDefault","symbolLocation":23527,"imageIndex":8},{"imageOffset":1181331,"imageIndex":8},{"imageOffset":274261,"symbol":"_PyFunction_Vectorcall","symbolLocation":261,"imageIndex":8},{"imageOffset":271954,"symbol":"_PyObject_FastCallDictTstate","symbolLocation":258,"imageIndex":8},{"imageOffset":275258,"symbol":"_PyObject_Call_Prepend","symbolLocation":154,"imageIndex":8},{"imageOffset":661632,"imageIndex":8},{"imageOffset":629620,"imageIndex":8},{"imageOffset":272432,"symbol":"_PyObject_MakeTpCall","symbolLocation":384,"imageIndex":8},{"imageOffset":1177680,"imageIndex":8},{"imageOffset":1164631,"symbol":"_PyEval_EvalFrameDefault","symbolLocation":23527,"imageIndex":8},{"imageOffset":274512,"imageIndex":8},{"imageOffset":1177467,"imageIndex":8},{"imageOffset":1164779,"symbol":"_PyEval_EvalFrameDefault","symbolLocation":23675,"imageIndex":8},{"imageOffset":1181331,"imageIndex":8},{"imageOffset":1140849,"symbol":"PyEval_EvalCode","symbolLocation":81,"imageIndex":8},{"imageOffset":1433249,"imageIndex":8},{"imageOffset":1433619,"imageIndex":8},{"imageOffset":1426084,"symbol":"PyRun_SimpleFileExFlags","symbolLocation":708,"imageIndex":8},{"imageOffset":1545968,"symbol":"Py_RunMain","symbolLocation":1840,"imageIndex":8},{"imageOffset":1547136,"imageIndex":8},{"imageOffset":1547227,"symbol":"Py_BytesMain","symbolLocation":43,"imageIndex":8},{"imageOffset":25413,"symbol":"start","symbolLocation":1909,"imageIndex":15}]},{"id":684449,"frames":[{"imageOffset":6816,"symbol":"start_wqthread","symbolLocation":0,"imageIndex":11}],"threadState":{"r13":{"value":0},"rax":{"value":33554800},"rflags":{"value":512},"cpu":{"value":0},"r14":{"value":1},"rsi":{"value":8707},"r8":{"value":5193730},"cr2":{"value":0},"rdx":{"value":123145383673856},"r10":{"value":0},"r9":{"value":1},"r15":{"value":123145384196984},"rbx":{"value":123145384198144},"trap":{"value":133},"err":{"value":33554800},"r11":{"value":582},"rip":{"value":140703503637152},"rbp":{"value":0},"rsp":{"value":123145384196976},"r12":{"value":5193734},"rcx":{"value":123145384196992},"flavor":"x86_THREAD_STATE","rdi":{"value":123145384198144}}},{"id":684450,"frames":[{"imageOffset":6816,"symbol":"start_wqthread","symbolLocation":0,"imageIndex":11}],"threadState":{"r13":{"value":0},"rax":{"value":33554800},"rflags":{"value":512},"cpu":{"value":0},"r14":{"value":1},"rsi":{"value":9475},"r8":{"value":5193730},"cr2":{"value":0},"rdx":{"value":123145384210432},"r10":{"value":0},"r9":{"value":1},"r15":{"value":123145384733560},"rbx":{"value":123145384734720},"trap":{"value":133},"err":{"value":33554800},"r11":{"value":582},"rip":{"value":140703503637152},"rbp":{"value":0},"rsp":{"value":123145384733552},"r12":{"value":5193734},"rcx":{"value":123145384733568},"flavor":"x86_THREAD_STATE","rdi":{"value":123145384734720}}},{"id":684469,"frames":[{"imageOffset":6816,"symbol":"start_wqthread","symbolLocation":0,"imageIndex":11}],"threadState":{"r13":{"value":0},"rax":{"value":33554800},"rflags":{"value":512},"cpu":{"value":0},"r14":{"value":1},"rsi":{"value":18947},"r8":{"value":409602},"cr2":{"value":0},"rdx":{"value":123145384747008},"r10":{"value":0},"r9":{"value":18446744073709551615},"r15":{"value":123145385270136},"rbx":{"value":123145385271296},"trap":{"value":133},"err":{"value":33554800},"r11":{"value":582},"rip":{"value":140703503637152},"rbp":{"value":0},"rsp":{"value":123145385271296},"r12":{"value":7094276},"rcx":{"value":0},"flavor":"x86_THREAD_STATE","rdi":{"value":123145385271296}}}],
  "usedImages" : [
  {
    "source" : "P",
    "arch" : "x86_64",
    "base" : 4439728128,
    "size" : 45056,
    "uuid" : "ae45d155-94e0-310e-94ce-1c2757018276",
    "path" : "\/Library\/Developer\/CommandLineTools\/Library\/Frameworks\/Python3.framework\/Versions\/3.9\/lib\/python3.9\/lib-dynload\/math.cpython-39-darwin.so",
    "name" : "math.cpython-39-darwin.so"
  },
  {
    "source" : "P",
    "arch" : "x86_64",
    "base" : 4439183360,
    "size" : 24576,
    "uuid" : "1bc366c2-bae5-397d-8114-abb2e23292bf",
    "path" : "\/Library\/Developer\/CommandLineTools\/Library\/Frameworks\/Python3.framework\/Versions\/3.9\/lib\/python3.9\/lib-dynload\/select.cpython-39-darwin.so",
    "name" : "select.cpython-39-darwin.so"
  },
  {
    "source" : "P",
    "arch" : "x86_64",
    "base" : 4439375872,
    "size" : 16384,
    "uuid" : "3bdb23d1-a50b-3d9e-a5c5-78f3c47cb6e5",
    "path" : "\/Library\/Developer\/CommandLineTools\/Library\/Frameworks\/Python3.framework\/Versions\/3.9\/lib\/python3.9\/lib-dynload\/_posixsubprocess.cpython-39-darwin.so",
    "name" : "_posixsubprocess.cpython-39-darwin.so"
  },
  {
    "source" : "P",
    "arch" : "x86_64",
    "base" : 4439322624,
    "size" : 12288,
    "uuid" : "78706dc5-d30c-3b28-8a69-9742b3a794c1",
    "path" : "\/Library\/Developer\/CommandLineTools\/Library\/Frameworks\/Python3.framework\/Versions\/3.9\/lib\/python3.9\/lib-dynload\/grp.cpython-39-darwin.so",
    "name" : "grp.cpython-39-darwin.so"
  },
  {
    "source" : "P",
    "arch" : "x86_64",
    "base" : 4437577728,
    "size" : 16384,
    "uuid" : "8e398855-3ad0-3316-b757-e6d055a773bc",
    "path" : "\/Library\/Developer\/CommandLineTools\/Library\/Frameworks\/Python3.framework\/Versions\/3.9\/lib\/python3.9\/lib-dynload\/_heapq.cpython-39-darwin.so",
    "name" : "_heapq.cpython-39-darwin.so"
  },
  {
    "source" : "P",
    "arch" : "x86_64",
    "base" : 4437790720,
    "size" : 40960,
    "uuid" : "78acc5ac-f6ff-3d92-b5f5-4d6ff805f14a",
    "path" : "\/Library\/Developer\/CommandLineTools\/Library\/Frameworks\/Python3.framework\/Versions\/3.9\/lib\/python3.9\/lib-dynload\/_tkinter.cpython-39-darwin.so",
    "name" : "_tkinter.cpython-39-darwin.so"
  },
  {
    "source" : "P",
    "arch" : "x86_64",
    "base" : 4437635072,
    "CFBundleShortVersionString" : "1.0",
    "CFBundleIdentifier" : "com.apple.IO80211",
    "size" : 16384,
    "uuid" : "822d5166-e0bd-394e-852c-50e775fe7277",
    "path" : "\/System\/Library\/PrivateFrameworks\/IO80211.framework\/Versions\/A\/IO80211",
    "name" : "IO80211",
    "CFBundleVersion" : "1"
  },
  {
    "source" : "P",
    "arch" : "x86_64",
    "base" : 4449837056,
    "size" : 344064,
    "uuid" : "d5ce0007-6e6e-383c-abe9-d66eb450ae2d",
    "path" : "\/System\/Library\/PrivateFrameworks\/IO80211.framework\/Versions\/A\/IO80211Old.dylib",
    "name" : "IO80211Old.dylib"
  },
  {
    "source" : "P",
    "arch" : "x86_64",
    "base" : 4446801920,
    "CFBundleShortVersionString" : "3.9.6",
    "CFBundleIdentifier" : "com.apple.python3",
    "size" : 2490368,
    "uuid" : "f8a6eb86-164c-36f7-97f2-8f6fadae8459",
    "path" : "\/Library\/Developer\/CommandLineTools\/Library\/Frameworks\/Python3.framework\/Versions\/3.9\/Python3",
    "name" : "Python3",
    "CFBundleVersion" : "3.9.6"
  },
  {
    "source" : "P",
    "arch" : "x86_64",
    "base" : 4435386368,
    "CFBundleShortVersionString" : "3.9.6",
    "CFBundleIdentifier" : "com.apple.python3",
    "size" : 8192,
    "uuid" : "c22a284e-5ae7-3332-95f5-de456ff5188e",
    "path" : "\/Library\/Developer\/CommandLineTools\/Library\/Frameworks\/Python3.framework\/Versions\/3.9\/Resources\/Python.app\/Contents\/MacOS\/Python",
    "name" : "Python",
    "CFBundleVersion" : "3.9.6"
  },
  {
    "source" : "P",
    "arch" : "x86_64",
    "base" : 140703503388672,
    "size" : 241656,
    "uuid" : "9419d8b3-682e-37c0-ace9-6125e601c289",
    "path" : "\/usr\/lib\/system\/libsystem_kernel.dylib",
    "name" : "libsystem_kernel.dylib"
  },
  {
    "source" : "P",
    "arch" : "x86_64",
    "base" : 140703503630336,
    "size" : 49152,
    "uuid" : "b299628a-6884-321f-b99a-46eaaa427093",
    "path" : "\/usr\/lib\/system\/libsystem_pthread.dylib",
    "name" : "libsystem_pthread.dylib"
  },
  {
    "source" : "P",
    "arch" : "x86_64",
    "base" : 140703502237696,
    "size" : 557056,
    "uuid" : "163b6214-c567-3d92-99e4-b85415fb81e2",
    "path" : "\/usr\/lib\/system\/libsystem_c.dylib",
    "name" : "libsystem_c.dylib"
  },
  {
    "source" : "P",
    "arch" : "x86_64",
    "base" : 140716540489728,
    "CFBundleShortVersionString" : "8.5.9",
    "CFBundleIdentifier" : "com.tcltk.tcllibrary",
    "size" : 823296,
    "uuid" : "89dfaddc-609e-36f2-af81-be2d7ab2d1ec",
    "path" : "\/System\/Library\/Frameworks\/Tcl.framework\/Versions\/8.5\/Tcl",
    "name" : "Tcl",
    "CFBundleVersion" : "8.5.9"
  },
  {
    "source" : "P",
    "arch" : "x86_64",
    "base" : 140716541927424,
    "CFBundleShortVersionString" : "8.5.9",
    "CFBundleIdentifier" : "com.tcltk.tklibrary",
    "size" : 929791,
    "uuid" : "faf894b5-455e-38d0-8ed0-340a1b17e4e3",
    "path" : "\/System\/Library\/Frameworks\/Tk.framework\/Versions\/8.5\/Tk",
    "name" : "Tk",
    "CFBundleVersion" : "8.5.9"
  },
  {
    "source" : "P",
    "arch" : "x86_64",
    "base" : 140703499911168,
    "size" : 592520,
    "uuid" : "14683982-4227-335b-bc68-561d947a8f73",
    "path" : "\/usr\/lib\/dyld",
    "name" : "dyld"
  },
  {
    "size" : 0,
    "source" : "A",
    "base" : 0,
    "uuid" : "00000000-0000-0000-0000-000000000000"
  }
],
  "sharedCache" : {
  "base" : 140703499214848,
  "size" : 25769803776,
  "uuid" : "4c1441fd-8a54-3dc2-863d-49110b946a25"
},
  "vmSummary" : "ReadOnly portion of Libraries: Total=435.3M resident=0K(0%) swapped_out_or_unallocated=435.3M(100%)\nWritable regions: Total=1.8G written=0K(0%) resident=0K(0%) swapped_out=0K(0%) unallocated=1.8G(100%)\n\n                                VIRTUAL   REGION \nREGION TYPE                        SIZE    COUNT (non-coalesced) \n===========                     =======  ======= \nActivity Tracing                   256K        1 \nColorSync                          156K       22 \nCoreServices                       148K        1 \nDispatch continuations            32.0M        1 \nKernel Alloc Once                    8K        1 \nMALLOC                            38.0M       24 \nMALLOC guard page                   32K        8 \nMALLOC_LARGE (reserved)            384K        1         reserved VM address space (unallocated)\nSTACK GUARD                         16K        4 \nStack                             17.5M        4 \nVM_ALLOCATE                       3336K       15 \nVM_ALLOCATE (reserved)             1.7G        2         reserved VM address space (unallocated)\n__DATA                            16.7M      319 \n__DATA_CONST                      15.2M      208 \n__DATA_DIRTY                       641K      103 \n__FONT_DATA                        2352        1 \n__LINKEDIT                       180.7M       12 \n__OBJC_RO                         71.9M        1 \n__OBJC_RW                         2201K        2 \n__TEXT                           254.6M      339 \nmapped file                       53.5M        7 \nshared memory                     1296K       18 \n===========                     =======  ======= \nTOTAL                              2.4G     1094 \nTOTAL, minus reserved VM space   688.0M     1094 \n",
  "legacyInfo" : {
  "threadTriggered" : {
    "queue" : "com.apple.main-thread"
  }
},
  "logWritingSignature" : "8f64c4aeeacf9de63a29416f2878979d71315625",
  "trialInfo" : {
  "rollouts" : [
    {
      "rolloutId" : "5ffde50ce2aacd000d47a95f",
      "factorPackIds" : {

      },
      "deploymentId" : 240000553
    },
    {
      "rolloutId" : "632c763c58740028737bfdd2",
      "factorPackIds" : {
        "SIRI_DIALOG_ASSETS" : "64a57d23fa6fd41b2353e2ae"
      },
      "deploymentId" : 240000034
    }
  ],
  "experiments" : [

  ]
}
}

Model: MacBookPro12,1, BootROM 489.0.0.0.0, 2 processors, Dual-Core Intel Core i5, 2.7 GHz, 16 GB, SMC 2.28f7
Graphics: Intel Iris Graphics 6100, Intel Iris Graphics 6100, Built-In
Display: Color LCD, 2560 x 1600 Retina, Main, MirrorOff, Online
Memory Module: BANK 0/DIMM0, 8 GB, DDR3, 1867 MHz, 0x02FE, 0x4544464232333241314D412D4A442D460000
Memory Module: BANK 1/DIMM0, 8 GB, DDR3, 1867 MHz, 0x02FE, 0x4544464232333241314D412D4A442D460000
AirPort: spairport_wireless_card_type_wifi (0x14E4, 0x133), Broadcom BCM43xx 1.0 (7.77.111.1 AirPortDriverBrcmNIC-1772.1)
AirPort: 
Bluetooth: Version (null), 0 services, 0 devices, 0 incoming serial ports
Network Service: Wi-Fi, AirPort, en0
Serial ATA Device: APPLE SSD SM0256G, 251 GB
USB Device: USB30Bus
USB Device: Bluetooth USB Host Controller
Thunderbolt Bus: MacBook Pro, Apple Inc., 27.1
