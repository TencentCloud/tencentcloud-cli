**Example 1: 查看工作流调度任务代码**

查看工作流调度任务代码

Input: 

```
tccli wedata GetTriggerTaskCode --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --TaskId 20251124113217312
```

Output: 
```
{
    "Response": {
        "Data": {
            "CodeFileSize": "288",
            "CodeInfo": "IyEvYmluL2Jhc2gKIyoqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKiMKIyNhdXRob3I6IHpoYW5nbGluCiMjY3JlYXRlIHRpbWU6IDIwMjQtMTItMDQgMTE6MTI6NDkKIyoqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKiMKaGVsbG93b3JsZAo="
        },
        "RequestId": "56a427fc-4b19-4d80-bd10-26a96bdfa140"
    }
}
```

