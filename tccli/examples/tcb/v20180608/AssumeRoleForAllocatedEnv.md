**Example 1: 获取环境对应的临时密钥**



Input: 

```
tccli tcb AssumeRoleForAllocatedEnv --cli-unfold-argument  \
    --EnvId mpdemo-d6ga2156e93c0228c
```

Output: 
```
{
    "Response": {
        "ExpiredTime": 1778249652,
        "IsCache": false,
        "SecretId": "AKI*****************************************************************",
        "SecretKey": "V4m*****************************************",
        "Token": "A6ABa1wqZnAFi95JuQ7BIgWqU8Im5YPa283df148910f67e4cb0789f5783133b4zHqyBHG_9fFGP1hqbOgzW4_f9P8vAUhxq6HpuxsWfSkJH5_qOUWwQiILad6W1zBDo-hFSyVoGPnwglEbflbwbpc6QQE5sjwq3ZAbfWmhVMZQB2RPqmJz3Gm0F-qKCsZjFAWn6xtmset1Md4CySETuQ2A-IsDC1tfQGEPMYOWW_X7IFchndIoLmqccAi27dJihlB_g7Bp009y7QCFICWFJdJ9uKzFdRu_A6FeXfvQGFGbPiMhYmo0LujgYHPOhYNZLMNbx7MdYoAh5lXCGodqKbu3S8z3GTYNftRHAUKxWC562IQ1QnyMyBEmUxNLabFsvefyYf_i27ZK1re4-xRfjF******************************************",
        "RequestId": "b07ee256-5624-4ce1-92ac-cc12d2a792ab"
    }
}
```

