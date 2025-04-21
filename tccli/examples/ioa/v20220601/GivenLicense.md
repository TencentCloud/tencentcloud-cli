**Example 1: 示例**

示例

Input: 

```
tccli ioa GivenLicense --cli-unfold-argument  \
    --GivenType TrialIOA \
    --Source Cwp \
    --InquireType DLP \
    --ContactNumber 13000000000
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "UnauthorizedOperation.PermissionDenied",
            "Message": "非企业用户"
        },
        "RequestId": "14d5aff4-7c99-497b-b248-52492b281b86"
    }
}
```

**Example 2: CWP iOA联合活动增送**



Input: 

```
tccli ioa GivenLicense --cli-unfold-argument  \
    --GivenType CwpUser \
    --Source Cwp
```

Output: 
```
{
    "Response": {
        "RequestId": "9f0a5ba9-19bb-4501-8439-7fe3542a1747"
    }
}
```

**Example 3: 示例1**

示例1

Input: 

```
tccli ioa GivenLicense --cli-unfold-argument  \
    --GivenType OfficialTrial \
    --Source Official \
    --InquireType Terminal \
    --ContactNumber 130000000 \
    --Name 王先生 \
    --Email 111@qq.com \
    --Focus 1 2 \
    --Company 公司 \
    --StaffNum 2
```

Output: 
```
{
    "Response": {
        "RequestId": "fde21647-5bde-49be-be2c-b5ea179b187d"
    }
}
```

**Example 4: 示例2**

示例2

Input: 

```
tccli ioa GivenLicense --cli-unfold-argument  \
    --GivenType OfficialTrial \
    --Source OfficialTrial \
    --InquireType Terminal \
    --ContactNumber 130000000 \
    --Name 王先生 \
    --Email 111@qq.com \
    --Focus 1 \
    --Company 1 \
    --StaffNum 1 \
    --Channel 1
```

Output: 
```
{
    "Response": {
        "RequestId": "8ba764e4-8cf4-4a48-90ae-62edc1eb525b"
    }
}
```

