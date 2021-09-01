**Example 1: 创建指向自己媒体的链接**

为媒体 ID 为 5fec3806b4e0960001ed9ce2  且属于自己的媒体创建链接，其分类路径为  /a/b 。

Input: 

```
tccli cme CreateLink --cli-unfold-argument  \
    --Platform test \
    --Type MATERIAL \
    --Name link \
    --ClassPath /a/b \
    --Owner.Id b4f5d76a1c4fbad03b26d258847c6217 \
    --Owner.Type PERSON \
    --DestinationId 5fec3806b4e0960001ed9ce2 \
    --DestinationOwner.Id b4f5d76a1c4fbad03b26d258847c6217 \
    --DestinationOwner.Type PERSON
```

Output: 
```
{
    "Response": {
        "MaterialId": "5fec3806b4e0960001ed9ce5",
        "RequestId": "d1c5eb0e-e499-4419-b465-60c097fbb65b"
    }
}
```

**Example 2: 创建指向别人媒体的链接**

为媒体 ID 为 5fec38060544f4e4260001ed9ce5 且属于用户 ID 为  38f5d76a1c4fbad03b26d258253fe468 的媒体创建链接，其分类路径为  /a/b 。

Input: 

```
tccli cme CreateLink --cli-unfold-argument  \
    --Platform test \
    --Type MATERIAL \
    --Name link \
    --ClassPath /a/b \
    --Owner.Id b4f5d76a1c4fbad03b26d258847c6217 \
    --Owner.Type PERSON \
    --DestinationId 5fec38060544f4e4260001ed9ce5 \
    --DestinationOwner.Id 38f5d76a1c4fbad03b26d258253fe468 \
    --DestinationOwner.Type PERSON
```

Output: 
```
{
    "Response": {
        "MaterialId": "5fec3806b4e0960001ed9ce6",
        "RequestId": "d1c5eb0e-e499-4419-b465-60c097fbb657"
    }
}
```

**Example 3: 创建指向别人团队媒体的链接**

为媒体 ID 为 5feb077183bac900010975bf 且属于团队 ID 为  cmetid_1eaea85c92e98f87ea8984441ae40280 的媒体创建链接，其分类路径为  /a/b 。

Input: 

```
tccli cme CreateLink --cli-unfold-argument  \
    --Platform test \
    --Type MATERIAL \
    --Name link \
    --ClassPath /a/b \
    --Owner.Id b4f5d76a1c4fbad03b26d258847c6217 \
    --Owner.Type PERSON \
    --DestinationId 5feb077183bac900010975bf \
    --DestinationOwner.Id cmetid_1eaea85c92e98f87ea8984441ae40280 \
    --DestinationOwner.Type TEAM
```

Output: 
```
{
    "Response": {
        "MaterialId": "5fec3806b4e0960001ed9ce6",
        "RequestId": "d1c5eb0e-e499-4419-b465-60c097fbb657"
    }
}
```

**Example 4: 创建指向分类的链接**

创建指向分类路径为 /a/c  的链接。

Input: 

```
tccli cme CreateLink --cli-unfold-argument  \
    --Platform test \
    --Type CLASS \
    --Name link \
    --ClassPath /a/b \
    --Owner.Id 38f5d76a1c4fbad03b26d258253fe468 \
    --Owner.Type PERSON \
    --DestinationId /a/c \
    --DestinationOwner.Id 38f5d76a1c4fbad03b26d258253fe468 \
    --DestinationOwner.Type PERSON
```

Output: 
```
{
    "Response": {
        "MaterialId": "5fec3806b4e0960001ed9ce61",
        "RequestId": "d1c5eb0e-e499-4419-b465-60c097fbb656"
    }
}
```

