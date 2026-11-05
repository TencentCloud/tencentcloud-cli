**Example 1: 下载活跃设备数量统计**

下载活跃设备数量统计

Input: 

```
tccli mna DownloadActiveDeviceCount --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "FilePath": "https://mpacc-1258344699.cos.ap-shanghai.myqcloud.com/statistics/mna_260126599_0_0_0__0.xlsx?x-cos-security-token=jU68plXgF9W2J2H1S65dWj5M92L4MYMaf02473be536abf52ddcf763a1f79d6ec3NtRhuCR7PprnY_BKjWs7IsQ65PACR3wCtoUlGvOOZGhvB7Oc8qNmSVExV2NkLY3p5x1kjEyZFldksTI9r5yXdW0rSTmlm_s2K4dgR0EWjjtFqNRHLczvIiSXX1K6uDAkiIhEIws-J3Y7VspAMumqJ7mR4L4Jim-zg7Hrrm9vD8zmE7w1k2v4a0fJbRe1NexAxD1sSRMFQnTumyVOliMPePO9p68NchKQjkmTGljZ1W8Epm-XmMR5l-gPlCY_CidmiVf0IrUXcw7mVHToePuaA&q-sign-algorithm=sha1&q-ak=AKID6dc7I7lfGY9lYY2dfzXSI0aO229ZuxrCCHmT55tQUxG2koB2icMWbsGKt9-GtHAV&q-sign-time=1789025741%3B1789029341&q-key-time=1789025741%3B1789029341&q-header-list=host&q-url-param-list=x-cos-security-token&q-signature=645a953502789db6e4a3d2a441d36a92b7139***",
        "RequestId": "5f5ada8a-c001-4f4c-a106-2e1b446a482f"
    }
}
```

**Example 2: 按应用下载活跃设备数量统计**

下载指定应用活跃设备数量统计

Input: 

```
tccli mna DownloadActiveDeviceCount --cli-unfold-argument  \
    --ApplicationId app-zdsbik***e
```

Output: 
```
{
    "Response": {
        "FilePath": "https://mpacc-1258344699.cos.ap-shanghai.myqcloud.com/statistics/mna_260126599_0_0_0_app-zdsbikjxye_0.xlsx?x-cos-security-token=jU68plXgF9W2J2H1S65dWj5M92L4MYMa2cee5338cec43a7fcdf6e26113ca72713NtRhuCR7PprnY_BKjWs7PDAdUqfAt-ZcTRfPzMVUEYLUvwokkq0DLIo4JRwG3xWTDAiIYrN3cn0vIOgCBl6lPh6C32yvnXe7CYZOxYfkN9AwyY7dOCoGo_6gPGhqFDqRkYePczlzAn-T2nw7lLq6jpJwcGqjOg-f848dU0N4MjM9tfwkyMbeqnvjF9FCAPhUmsOAgN5btgq4xjOL6DbKBAOGEEMRYzvCDll0ZbH181PEhefLKwap6R_8b2Rx0iMpfvcyrFpFh_dXXqH4I0uYg&q-sign-algorithm=sha1&q-ak=AKIDE3f-9xNAn3Wr3onltY-A-KDWm55BDEz59qt0v-hXO9rcgb4-VGpzWheGVSK6SpmT&q-sign-time=1789025768%3B1789029368&q-key-time=17890257*****1789029368&q-header-list=host&q-url-param-list=x-cos-security-token&q-signature=6cf33f214ae8c10588415ab8820b17b7765b****",
        "RequestId": "d798fe11-7809-4319-a686-79887f932424"
    }
}
```

