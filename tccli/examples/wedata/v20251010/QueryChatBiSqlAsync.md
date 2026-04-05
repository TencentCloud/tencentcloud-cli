**Example 1: ChatBI下发sql异步查询**

ChatBI下发sql异步查询

Input: 

```
tccli wedata QueryChatBiSqlAsync --cli-unfold-argument  \
    --RoomKey 717cf6d9b66843821763518902826abd2ab94923f4add \
    --WorkspaceId 202511191030 \
    --Sql SELECT * FROM `employees_1w` LIMIT 100 \
    --AsyncTaskId task_4e8469ffe2984d338b08f8dcfa217462
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskId": "task_4e8469ffe2984d338b08f8dcfa217462",
            "TaskStatus": "SUCCESS",
            "Data": {
                "Objects": "[{\"name\":\"Frank\",\"id\":\"1\",\"department\":\"Sales\",\"salary\":\"76954\"},{\"name\":\"Vince\",\"id\":\"2\",\"department\":\"Sales\",\"salary\":\"73001\"},{\"name\":\"Tom\",\"id\":\"3\",\"department\":\"R&D\",\"salary\":\"66578\"},{\"name\":\"Uma\",\"id\":\"4\",\"department\":\"Operations\",\"salary\":\"79157\"},{\"name\":\"Ivy\",\"id\":\"5\",\"department\":\"HR\",\"salary\":\"51392\"},{\"name\":\"Amy\",\"id\":\"6\",\"department\":\"Sales\",\"salary\":\"121814\"},{\"name\":\"Wendy\",\"id\":\"7\",\"department\":\"Legal\",\"salary\":\"92665\"},{\"name\":\"Henry\",\"id\":\"8\",\"department\":\"Sales\",\"salary\":\"55829\"},{\"name\":\"Cathy\",\"id\":\"9\",\"department\":\"Sales\",\"salary\":\"57637\"},{\"name\":\"Xander\",\"id\":\"10\",\"department\":\"R&D\",\"salary\":\"144300\"},{\"name\":\"Xander\",\"id\":\"11\",\"department\":\"Customer Service\",\"salary\":\"126807\"},{\"name\":\"Eva\",\"id\":\"12\",\"department\":\"Customer Service\",\"salary\":\"104594\"},{\"name\":\"Ivy\",\"id\":\"13\",\"department\":\"Marketing\",\"salary\":\"79411\"},{\"name\":\"Cathy\",\"id\":\"14\",\"department\":\"R&D\",\"salary\":\"117903\"},{\"name\":\"Paul\",\"id\":\"15\",\"department\":\"R&D\",\"salary\":\"103864\"},{\"name\":\"Uma\",\"id\":\"16\",\"department\":\"Finance\",\"salary\":\"87172\"},{\"name\":\"Zack\",\"id\":\"17\",\"department\":\"R&D\",\"salary\":\"134800\"},{\"name\":\"Sophia\",\"id\":\"18\",\"department\":\"HR\",\"salary\":\"134498\"},{\"name\":\"Bob\",\"id\":\"19\",\"department\":\"IT\",\"salary\":\"138027\"},{\"name\":\"Eva\",\"id\":\"20\",\"department\":\"R&D\",\"salary\":\"121544\"},{\"name\":\"Cathy\",\"id\":\"21\",\"department\":\"R&D\",\"salary\":\"73014\"},{\"name\":\"Nick\",\"id\":\"22\",\"department\":\"Sales\",\"salary\":\"55865\"},{\"name\":\"Yara\",\"id\":\"23\",\"department\":\"Engineering\",\"salary\":\"55591\"},{\"name\":\"Nick\",\"id\":\"24\",\"department\":\"R&D\",\"salary\":\"86250\"},{\"name\":\"Vince\",\"id\":\"25\",\"department\":\"Finance\",\"salary\":\"117513\"},{\"name\":\"Dan\",\"id\":\"26\",\"department\":\"Finance\",\"salary\":\"141269\"},{\"name\":\"Sophia\",\"id\":\"27\",\"department\":\"Legal\",\"salary\":\"87382\"},{\"name\":\"Yara\",\"id\":\"28\",\"department\":\"IT\",\"salary\":\"53806\"},{\"name\":\"David\",\"id\":\"29\",\"department\":\"Customer Service\",\"salary\":\"98666\"},{\"name\":\"Cathy\",\"id\":\"30\",\"department\":\"IT\",\"salary\":\"141497\"},{\"name\":\"Eva\",\"id\":\"31\",\"department\":\"HR\",\"salary\":\"83951\"},{\"name\":\"Charlie\",\"id\":\"32\",\"department\":\"Legal\",\"salary\":\"56398\"},{\"name\":\"David\",\"id\":\"33\",\"department\":\"Marketing\",\"salary\":\"67207\"},{\"name\":\"Wendy\",\"id\":\"34\",\"department\":\"R&D\",\"salary\":\"129545\"},{\"name\":\"Ivy\",\"id\":\"35\",\"department\":\"Customer Service\",\"salary\":\"69718\"},{\"name\":\"Wendy\",\"id\":\"36\",\"department\":\"Customer Service\",\"salary\":\"101990\"},{\"name\":\"Uma\",\"id\":\"37\",\"department\":\"HR\",\"salary\":\"143663\"},{\"name\":\"Uma\",\"id\":\"38\",\"department\":\"R&D\",\"salary\":\"128143\"},{\"name\":\"Charlie\",\"id\":\"39\",\"department\":\"HR\",\"salary\":\"127067\"},{\"name\":\"Vince\",\"id\":\"40\",\"department\":\"Customer Service\",\"salary\":\"114483\"},{\"name\":\"Paul\",\"id\":\"41\",\"department\":\"Finance\",\"salary\":\"106547\"},{\"name\":\"Dan\",\"id\":\"42\",\"department\":\"Customer Service\",\"salary\":\"121774\"},{\"name\":\"Karen\",\"id\":\"43\",\"department\":\"Legal\",\"salary\":\"72058\"},{\"name\":\"Alice\",\"id\":\"44\",\"department\":\"IT\",\"salary\":\"135523\"},{\"name\":\"Nick\",\"id\":\"45\",\"department\":\"Engineering\",\"salary\":\"144250\"},{\"name\":\"Ivy\",\"id\":\"46\",\"department\":\"Sales\",\"salary\":\"117790\"},{\"name\":\"Eva\",\"id\":\"47\",\"department\":\"Operations\",\"salary\":\"56270\"},{\"name\":\"Sophia\",\"id\":\"48\",\"department\":\"Marketing\",\"salary\":\"109997\"},{\"name\":\"Grace\",\"id\":\"49\",\"department\":\"Legal\",\"salary\":\"57142\"},{\"name\":\"Henry\",\"id\":\"50\",\"department\":\"Finance\",\"salary\":\"129236\"},{\"name\":\"Nick\",\"id\":\"51\",\"department\":\"Finance\",\"salary\":\"105385\"},{\"name\":\"David\",\"id\":\"52\",\"department\":\"Engineering\",\"salary\":\"114194\"},{\"name\":\"Charlie\",\"id\":\"53\",\"department\":\"Finance\",\"salary\":\"118597\"},{\"name\":\"Jack\",\"id\":\"54\",\"department\":\"Finance\",\"salary\":\"77542\"},{\"name\":\"Cathy\",\"id\":\"55\",\"department\":\"Engineering\",\"salary\":\"73582\"},{\"name\":\"Queen\",\"id\":\"56\",\"department\":\"Engineering\",\"salary\":\"125317\"},{\"name\":\"Jack\",\"id\":\"57\",\"department\":\"HR\",\"salary\":\"119373\"},{\"name\":\"Bob\",\"id\":\"58\",\"department\":\"Legal\",\"salary\":\"82810\"},{\"name\":\"David\",\"id\":\"59\",\"department\":\"Customer Service\",\"salary\":\"92688\"},{\"name\":\"Grace\",\"id\":\"60\",\"department\":\"Operations\",\"salary\":\"120147\"},{\"name\":\"Vince\",\"id\":\"61\",\"department\":\"IT\",\"salary\":\"103379\"},{\"name\":\"Charlie\",\"id\":\"62\",\"department\":\"R&D\",\"salary\":\"116213\"},{\"name\":\"Queen\",\"id\":\"63\",\"department\":\"Legal\",\"salary\":\"133610\"},{\"name\":\"Nick\",\"id\":\"64\",\"department\":\"IT\",\"salary\":\"126862\"},{\"name\":\"Eva\",\"id\":\"65\",\"department\":\"IT\",\"salary\":\"99573\"},{\"name\":\"Alice\",\"id\":\"66\",\"department\":\"Customer Service\",\"salary\":\"74786\"},{\"name\":\"Dan\",\"id\":\"67\",\"department\":\"Sales\",\"salary\":\"96131\"},{\"name\":\"Frank\",\"id\":\"68\",\"department\":\"HR\",\"salary\":\"87021\"},{\"name\":\"Leo\",\"id\":\"69\",\"department\":\"HR\",\"salary\":\"130892\"},{\"name\":\"Mona\",\"id\":\"70\",\"department\":\"Sales\",\"salary\":\"146622\"},{\"name\":\"Mona\",\"id\":\"71\",\"department\":\"Operations\",\"salary\":\"60695\"},{\"name\":\"Bob\",\"id\":\"72\",\"department\":\"R&D\",\"salary\":\"73032\"},{\"name\":\"Amy\",\"id\":\"73\",\"department\":\"Marketing\",\"salary\":\"116911\"},{\"name\":\"Queen\",\"id\":\"74\",\"department\":\"Customer Service\",\"salary\":\"144761\"},{\"name\":\"Mona\",\"id\":\"75\",\"department\":\"R&D\",\"salary\":\"125375\"},{\"name\":\"Amy\",\"id\":\"76\",\"department\":\"Marketing\",\"salary\":\"115371\"},{\"name\":\"Vince\",\"id\":\"77\",\"department\":\"Operations\",\"salary\":\"64287\"},{\"name\":\"Xander\",\"id\":\"78\",\"department\":\"Engineering\",\"salary\":\"99721\"},{\"name\":\"Karen\",\"id\":\"79\",\"department\":\"Sales\",\"salary\":\"80235\"},{\"name\":\"Xander\",\"id\":\"80\",\"department\":\"Finance\",\"salary\":\"85910\"},{\"name\":\"Mona\",\"id\":\"81\",\"department\":\"Engineering\",\"salary\":\"115990\"},{\"name\":\"Henry\",\"id\":\"82\",\"department\":\"R&D\",\"salary\":\"144203\"},{\"name\":\"Yara\",\"id\":\"83\",\"department\":\"Legal\",\"salary\":\"74626\"},{\"name\":\"Ben\",\"id\":\"84\",\"department\":\"HR\",\"salary\":\"96230\"},{\"name\":\"Grace\",\"id\":\"85\",\"department\":\"Finance\",\"salary\":\"87657\"},{\"name\":\"Wendy\",\"id\":\"86\",\"department\":\"Engineering\",\"salary\":\"64295\"},{\"name\":\"Eva\",\"id\":\"87\",\"department\":\"IT\",\"salary\":\"69744\"},{\"name\":\"Uma\",\"id\":\"88\",\"department\":\"R&D\",\"salary\":\"60696\"},{\"name\":\"Ben\",\"id\":\"89\",\"department\":\"Operations\",\"salary\":\"97827\"},{\"name\":\"Ben\",\"id\":\"90\",\"department\":\"Customer Service\",\"salary\":\"119892\"},{\"name\":\"Olivia\",\"id\":\"91\",\"department\":\"Sales\",\"salary\":\"138272\"},{\"name\":\"Yara\",\"id\":\"92\",\"department\":\"Marketing\",\"salary\":\"67251\"},{\"name\":\"David\",\"id\":\"93\",\"department\":\"Engineering\",\"salary\":\"113077\"},{\"name\":\"Grace\",\"id\":\"94\",\"department\":\"Finance\",\"salary\":\"143517\"},{\"name\":\"Yara\",\"id\":\"95\",\"department\":\"R&D\",\"salary\":\"110228\"},{\"name\":\"Mona\",\"id\":\"96\",\"department\":\"Engineering\",\"salary\":\"61857\"},{\"name\":\"Leo\",\"id\":\"97\",\"department\":\"Operations\",\"salary\":\"147816\"},{\"name\":\"Charlie\",\"id\":\"98\",\"department\":\"Sales\",\"salary\":\"74117\"},{\"name\":\"Jack\",\"id\":\"99\",\"department\":\"IT\",\"salary\":\"126850\"},{\"name\":\"Wendy\",\"id\":\"100\",\"department\":\"Finance\",\"salary\":\"56144\"}]",
                "Sql": "SELECT * FROM `employees_1w` LIMIT 100",
                "Total": "100",
                "CostTime": 9586,
                "CreateTime": "",
                "Columns": [
                    {
                        "Name": "id",
                        "Type": "integer",
                        "Comment": ""
                    },
                    {
                        "Name": "name",
                        "Type": "string",
                        "Comment": ""
                    },
                    {
                        "Name": "department",
                        "Type": "string",
                        "Comment": ""
                    },
                    {
                        "Name": "salary",
                        "Type": "integer",
                        "Comment": ""
                    }
                ]
            },
            "ErrorMessage": "",
            "Duration": "18103"
        },
        "RequestId": "9010830d-bfba-4610-ab8f-314193d9bb22"
    }
}
```

