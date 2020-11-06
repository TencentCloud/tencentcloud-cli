**Example 1: 共享信息新增**



Input: 

```
tccli tbaas SrvInvoke --cli-unfold-argument  \
    --Module trustsql_mng \
    --Operation SrvInvoke \
    --Service iss \
    --Method Iss_Append \
    --Param "mch_sign":"MEQCID0FuZnQUmzTFlokvIOr0WOhraDMAKRuyolhuy2O/dX4AiBsM23VBz8eCQ50KW3cMPj/HpejQ6FL427uW9DDFdmRvw
```

Output: 
```
{
    "Response": {
        "RetCode": 0,
        "RetMsg": "ok",
        "Data": {
            "version": "2.0",
            "sign_type": "ECDSA",
            "mch_id": "trust_mch",
            "mch_sign": "MEYCIQDo4IOwpxsHApDU7XZTBOG4LbT2oJCG0FGV53j7JF3nNwIhAIXbE2sPKGYIbZ7riixirww5UPBL9mvXxQQyjxlOHY4V",
            "retcode": 0,
            "retmsg": "SUCCESS",
            "t_hash": "30dd11831f35855e2f9fe32933333b00f44af0111b46216dd6462da46c3313d8",
            "b_height": "107234",
            "b_time": "2018-09-03 14:27:07"
        }
    }
}
```

