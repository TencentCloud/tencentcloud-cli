**Example 1: 进行会话**

会话

Input: 

```
tccli fibona SendComponentSession --cli-unfold-argument  \
    --UserGroupUniqueID rum-M2seOxn4Cn4YlQVMp \
    --SessionID 619 \
    --Clues {"崩溃设备信息":[{"content":"机型：ALN-AL80(proportion:100%)\n      应用类型(开发平台)：harmonyos(proportion:100%)\n      CPU架构：arm64-v8a(proportion:100%)\n      系统版本：OpenHarmony-5.0.1.73(Beta1)(proportion:100%)\n      崩溃时应用在前/后台：foreground(proportion:100%) \n      "}],"崩溃问题原因":[{"content":"native_crash | signal 11(SIGSEGV), code 1(SEGV_MAPERR), address 0x0000000000000100"}],"崩溃线程堆栈":[{"content":"000000000000617c /data/storage/el1/bundle/libs/arm64/"}]}
```

Output: 
```
{
    "code": 0,
    "data": {
        "action": "root:done",
        "finished": true,
        "meta_data": {}
    },
    "msg": "success"
}
```

