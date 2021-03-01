**Example 1: 创建普通剪辑项目**



Input: 

```
tccli cme CreateProject --cli-unfold-argument  \
    --Platform test \
    --Category VIDEO_EDIT \
    --Name first_project \
    --Owner.Id 1111 \
    --Owner.Type PERSON \
    --AspectRatio 16:9
```

Output: 
```
{
    "Response": {
        "ProjectId": "cmepid_5f16967b64436100015fb025",
        "RequestId": "c44cbb5b-b809-4061-8c45-7469b64e8e5x"
    }
}
```

**Example 2: 创建一个导播台项目**



Input: 

```
tccli cme CreateProject --cli-unfold-argument  \
    --Platform test \
    --Category SWITCHER \
    --Name switcher_project \
    --Owner.Id 1111 \
    --Owner.Type PERSON \
    --SwitcherProjectInput.PgmOutputConfig.TemplateId 10001
```

Output: 
```
{
    "Response": {
        "ProjectId": "3f1699f3f97b9f0001920f29",
        "RequestId": "c44cbb5b-b809-4061-8c45-7469b64e8e5c"
    }
}
```

