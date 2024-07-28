**Example 1: 动作库列表查询**

动作库列表数据查询

Input: 

```
tccli cfg DescribeActionLibraryList --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0 \
    --Filters.0.Keyword a_type \
    --Filters.0.Values 1 \
    --ObjectType 1 \
    --Attribute 1
```

Output: 
```
{
    "Response": {
        "RequestId": "cZ6m0xYnnDreBNJm",
        "Results": [
            {
                "ActionName": "关机（测试）",
                "Desc": "对CVM进行关机操作",
                "ActionType": "平台",
                "CreateTime": "2023-07-04 11:20:43",
                "Creator": "系统",
                "UpdateTime": "2023-07-04 11:20:43",
                "RiskDesc": "高风险",
                "ActionId": 1,
                "AttributeId": 1,
                "RelationActionId": 2,
                "ActionCommand": "调用腾讯云对应产品的API接口",
                "ActionContent": "调用云api StopInstances",
                "ActionCommandType": 1,
                "ActionDetail": "<p>调用云api <a href=\"https://cloud.tencent.com/document/product/213/15743\">StopInstances</a>关机</p>",
                "ResourceType": "服务器资源",
                "IsAllowed": true,
                "ActionBestCase": "https://cloud.tencent.com/document/product/1500/74357",
                "ObjectType": "CVM",
                "MetricIdList": [
                    614,
                    615
                ]
            },
            {
                "ActionName": "开机",
                "Desc": "对CVM进行开机操作",
                "ActionType": "平台",
                "CreateTime": "2022-11-29 18:08:46",
                "Creator": "系统",
                "UpdateTime": "2022-11-29 18:08:46",
                "RiskDesc": "高风险",
                "ActionId": 2,
                "AttributeId": 2,
                "RelationActionId": 1,
                "ActionCommand": "调用腾讯云对应产品的API接口",
                "ActionContent": "调用云api StartInstances",
                "ActionCommandType": 1,
                "ActionDetail": "<p>调用云api <a href=\"https://cloud.tencent.com/document/product/213/15735\">StartInstances</a>开机</p>",
                "ResourceType": "服务器资源",
                "IsAllowed": true,
                "ActionBestCase": "",
                "ObjectType": "CVM",
                "MetricIdList": []
            },
            {
                "ActionName": "重启",
                "Desc": "重启",
                "ActionType": "平台",
                "CreateTime": "2023-05-24 15:33:39",
                "Creator": "系统",
                "UpdateTime": "2023-05-24 15:33:39",
                "RiskDesc": "高风险",
                "ActionId": 3,
                "AttributeId": 1,
                "RelationActionId": 0,
                "ActionCommand": "调用腾讯云对应产品的API接口",
                "ActionContent": "调用云api RebootInstances",
                "ActionCommandType": 1,
                "ActionDetail": "<p>调用云api <a href=\"https://cloud.tencent.com/document/product/213/15742\">RebootInstances</a>重启</p>",
                "ResourceType": "服务器资源",
                "IsAllowed": true,
                "ActionBestCase": "https://tcloud4api.woa.com/document/product/1607/88863?!preview&!document=1",
                "ObjectType": "CVM",
                "MetricIdList": []
            },
            {
                "ActionName": "CPU利用率高",
                "Desc": "使用stress-ng压测工具压测，支持的linux发行版：Centos7.2及以上，CoreOS 1745.5.0及以上，Debian9.0及以上，Ubuntu 16.04.1及以上",
                "ActionType": "平台",
                "CreateTime": "2022-11-29 18:08:46",
                "Creator": "系统",
                "UpdateTime": "2022-11-29 18:08:46",
                "RiskDesc": "高风险",
                "ActionId": 4,
                "AttributeId": 1,
                "RelationActionId": 0,
                "ActionCommand": "#!/bin/bash\n\nuser=$(whoami)\nif [ !$user == 'root' ]\nthen\n    sudo -i\nfi\n\nfunction command_exists(){\n    if command -v $1 > /dev/null 2>&1; then\n        return 1\n    else\n        return 0\n    fi\n}\n\necho -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\n\nos_desc=$(cat /etc/*release)\n# echo $os_desc\n\ndeclare -A os_dic\nos_dic=([CentOS]=\"yum install stress-ng -y\" \\\n        [CoreOS]=\"docker pull alexeiled/stress-ng\" \\\n        [Debian]=\"apt-get install -y stress-ng\" \\\n        [Ubuntu]=\"apt-get install -y stress-ng\")\n\nos_name='N/A'\n\nfor key in $(echo ${!os_dic[*]})\ndo\n    if [[ $os_desc =~ $key ]]\n    then\n        os_name=$key\n        echo $key\n    fi\ndone\n\nif [ $os_name == 'N/A' ]\nthen\n    echo \"Unsupported Linux distributions\"\n    exit 1\nfi\n\n# os_name=$(cat /etc/*release | awk 'NR==1{print($1)}')\n\necho -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\necho \"installing stress-ng...\"\ncommand_exists stress-ng\n\nif [[ $? -eq 0 ]]\nthen\n    ${os_dic[$os_name]}\n    echo -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\n    echo \"Checking the installation status...\"\n    command_exists stress-ng\n    if [[ $? -eq 0 && $os_name != 'CoreOS' ]]\n    then\n        echo -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\n        echo \"Fail to install\"\n        exit 1\n    else\n        echo -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\n        echo \"stress-ng has already installed\"\n    fi\nelse\n    echo -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\n    echo \"stress-ng has already installed\"\nfi\n\necho -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\necho \"Starting to perform stress test.\"\nif [ $os_name == \"CoreOS\" ]\nthen\n    docker run --rm alexeiled/stress-ng -c 0 -l {{percentage}} --timeout {{timeout}}\nelse\n    stress-ng -c 0 -l {{percentage}} --timeout {{timeout}}\nfi\n\nif [[ !$? -eq 0 ]]\nthen\n    echo -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\n    echo \"failed\"\n    exit 1\nelse\n    echo -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\n    echo \"completed\"\n    exit 0\nfi",
                "ActionContent": "#!/bin/bash\n\nuser=$(whoami)\nif [ !$user == 'root' ]\nthen\n    sudo -i\nfi\n\nfunction command_exists(){\n    if command -v $1 > /dev/null 2>&1; then\n        return 1\n    else\n        return 0\n    fi\n}\n\necho -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\n\nos_desc=$(cat /etc/*release)\n# echo $os_desc\n\ndeclare -A os_dic\nos_dic=([CentOS]=\"yum install stress-ng -y\" \\\n        [CoreOS]=\"docker pull alexeiled/stress-ng\" \\\n        [Debian]=\"apt-get install -y stress-ng\" \\\n        [Ubuntu]=\"apt-get install -y stress-ng\")\n\nos_name='N/A'\n\nfor key in $(echo ${!os_dic[*]})\ndo\n    if [[ $os_desc =~ $key ]]\n    then\n        os_name=$key\n        echo $key\n    fi\ndone\n\nif [ $os_name == 'N/A' ]\nthen\n    echo \"Unsupported Linux distributions\"\n    exit 1\nfi\n\n# os_name=$(cat /etc/*release | awk 'NR==1{print($1)}')\n\necho -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\necho \"installing stress-ng...\"\ncommand_exists stress-ng\n\nif [[ $? -eq 0 ]]\nthen\n    ${os_dic[$os_name]}\n    echo -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\n    echo \"Checking the installation status...\"\n    command_exists stress-ng\n    if [[ $? -eq 0 && $os_name != 'CoreOS' ]]\n    then\n        echo -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\n        echo \"Fail to install\"\n        exit 1\n    else\n        echo -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\n        echo \"stress-ng has already installed\"\n    fi\nelse\n    echo -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\n    echo \"stress-ng has already installed\"\nfi\n\necho -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\necho \"Starting to perform stress test.\"\nif [ $os_name == \"CoreOS\" ]\nthen\n    docker run --rm alexeiled/stress-ng -c 0 -l {{percentage}} --timeout {{timeout}}\nelse\n    stress-ng -c 0 -l {{percentage}} --timeout {{timeout}}\nfi\n\nif [[ !$? -eq 0 ]]\nthen\n    echo -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\n    echo \"failed\"\n    exit 1\nelse\n    echo -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\n    echo \"completed\"\n    exit 0\nfi",
                "ActionCommandType": 0,
                "ActionDetail": "<p>使用tat通道下发stress-ng命令进行压测</p>\n<p>命令内容：stress-ng -c 0 -l {{percentage}} --timeout {{timeout}}</p>\n<p><a href=\"https://cloud.tencent.com/document/api/1340/52676\">tat官方文档</a></p>\n<p><a href=\"https://wiki.ubuntu.com/Kernel/Reference/stress-ng\">stress-ng官方文档</a></p>\n",
                "ResourceType": "CPU资源",
                "IsAllowed": true,
                "ActionBestCase": "",
                "ObjectType": "CVM",
                "MetricIdList": []
            },
            {
                "ActionName": "内存利用率高",
                "Desc": "使用stress-ng压测工具压测，支持的linux发行版：Centos7.2及以上，CoreOS 1745.5.0及以上，Debian9.0及以上，Ubuntu 16.04.1及以上",
                "ActionType": "平台",
                "CreateTime": "2022-11-29 18:08:46",
                "Creator": "系统",
                "UpdateTime": "2022-11-29 18:08:46",
                "RiskDesc": "高风险",
                "ActionId": 7,
                "AttributeId": 1,
                "RelationActionId": 0,
                "ActionCommand": "#!/bin/bash\n\nuser=$(whoami)\nif [ !$user == 'root' ]\nthen\n    sudo -i\nfi\n\nfunction command_exists(){\n    if command -v $1 > /dev/null 2>&1; then\n        return 1\n    else\n        return 0\n    fi\n}\n\necho -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\n\nos_desc=$(cat /etc/*release)\n# echo $os_desc\n\ndeclare -A os_dic\nos_dic=([CentOS]=\"yum install stress-ng -y\" \\\n        [CoreOS]=\"docker pull alexeiled/stress-ng\" \\\n        [Debian]=\"apt-get install -y stress-ng\" \\\n        [Ubuntu]=\"apt-get install -y stress-ng\")\n\nos_name='N/A'\n\nfor key in $(echo ${!os_dic[*]})\ndo\n    if [[ $os_desc =~ $key ]]\n    then\n        os_name=$key\n        echo $key\n    fi\ndone\n\nif [ $os_name == 'N/A' ]\nthen\n    echo \"Unsupported Linux distributions\"\n    exit 1\nfi\n\n# os_name=$(cat /etc/*release | awk 'NR==1{print($1)}')\n\necho -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\necho \"installing stress-ng...\"\ncommand_exists stress-ng\n\nif [[ $? -eq 0 ]]\nthen\n    ${os_dic[$os_name]}\n    echo -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\n    echo \"Checking the installation status...\"\n    command_exists stress-ng\n    if [[ $? -eq 0 && $os_name != 'CoreOS' ]]\n    then\n        echo -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\n        echo \"Fail to install\"\n        exit 1\n    else\n        echo -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\n        echo \"stress-ng has already installed\"\n    fi\nelse\n    echo -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\n    echo \"stress-ng has already installed\"\nfi\n\necho -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\necho \"Starting to perform stress test\"\nif [ $os_name == \"CoreOS\" ]\nthen\n    docker run --rm alexeiled/stress-ng --vm-bytes $(awk '/MemAvailable/{printf \"%d\\n\", $2 * 0.01*{{percentage}};}' < /proc/meminfo)k --vm-keep -m 1 -t {{timeout}}\nelse\n    avaliable_mem=$(awk '/^MemAvailable:/{printf \"%d\\n\", $2;}' < /proc/meminfo)\n    free_mem=$(awk '/^MemFree:/{printf \"%d\\n\", $2;}' < /proc/meminfo)\n    buffer=$(awk '/^Buffers:/{printf \"%d\\n\", $2;}' < /proc/meminfo)\n    cache=$(awk '/^Cached:/{printf \"%d\\n\", $2;}' < /proc/meminfo)\n    if [ -n \"$avaliable_mem\" ]\n    then\n        stress-ng --vm-bytes $[$avaliable_mem*{{percentage}}/100]k --vm-keep -m 1 -t {{timeout}}\n    else\n        stress-ng --vm-bytes $[($free_mem+$buffer+$cache)*{{percentage}}/100]k --vm-keep -m 1 -t {{timeout}}\n    fi\nfi\n\nif [[ !$? -eq 0 ]]\nthen\n    echo -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\n    echo \"Failed\"\n    exit 1\nelse\n    echo -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\n    echo \"Completed\"\n    exit 0\nfi",
                "ActionContent": "#!/bin/bash\n\nuser=$(whoami)\nif [ !$user == 'root' ]\nthen\n    sudo -i\nfi\n\nfunction command_exists(){\n    if command -v $1 > /dev/null 2>&1; then\n        return 1\n    else\n        return 0\n    fi\n}\n\necho -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\n\nos_desc=$(cat /etc/*release)\n# echo $os_desc\n\ndeclare -A os_dic\nos_dic=([CentOS]=\"yum install stress-ng -y\" \\\n        [CoreOS]=\"docker pull alexeiled/stress-ng\" \\\n        [Debian]=\"apt-get install -y stress-ng\" \\\n        [Ubuntu]=\"apt-get install -y stress-ng\")\n\nos_name='N/A'\n\nfor key in $(echo ${!os_dic[*]})\ndo\n    if [[ $os_desc =~ $key ]]\n    then\n        os_name=$key\n        echo $key\n    fi\ndone\n\nif [ $os_name == 'N/A' ]\nthen\n    echo \"Unsupported Linux distributions\"\n    exit 1\nfi\n\n# os_name=$(cat /etc/*release | awk 'NR==1{print($1)}')\n\necho -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\necho \"installing stress-ng...\"\ncommand_exists stress-ng\n\nif [[ $? -eq 0 ]]\nthen\n    ${os_dic[$os_name]}\n    echo -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\n    echo \"Checking the installation status...\"\n    command_exists stress-ng\n    if [[ $? -eq 0 && $os_name != 'CoreOS' ]]\n    then\n        echo -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\n        echo \"Fail to install\"\n        exit 1\n    else\n        echo -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\n        echo \"stress-ng has already installed\"\n    fi\nelse\n    echo -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\n    echo \"stress-ng has already installed\"\nfi\n\necho -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\necho \"Starting to perform stress test\"\nif [ $os_name == \"CoreOS\" ]\nthen\n    docker run --rm alexeiled/stress-ng --vm-bytes $(awk '/MemAvailable/{printf \"%d\\n\", $2 * 0.01*{{percentage}};}' < /proc/meminfo)k --vm-keep -m 1 -t {{timeout}}\nelse\n    avaliable_mem=$(awk '/^MemAvailable:/{printf \"%d\\n\", $2;}' < /proc/meminfo)\n    free_mem=$(awk '/^MemFree:/{printf \"%d\\n\", $2;}' < /proc/meminfo)\n    buffer=$(awk '/^Buffers:/{printf \"%d\\n\", $2;}' < /proc/meminfo)\n    cache=$(awk '/^Cached:/{printf \"%d\\n\", $2;}' < /proc/meminfo)\n    if [ -n \"$avaliable_mem\" ]\n    then\n        stress-ng --vm-bytes $[$avaliable_mem*{{percentage}}/100]k --vm-keep -m 1 -t {{timeout}}\n    else\n        stress-ng --vm-bytes $[($free_mem+$buffer+$cache)*{{percentage}}/100]k --vm-keep -m 1 -t {{timeout}}\n    fi\nfi\n\nif [[ !$? -eq 0 ]]\nthen\n    echo -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\n    echo \"Failed\"\n    exit 1\nelse\n    echo -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\n    echo \"Completed\"\n    exit 0\nfi",
                "ActionCommandType": 0,
                "ActionDetail": "<p>使用tat通道下发stress-ng命令进行压测</p>\n<p>命令内容：stress-ng --vm-bytes $(awk '/MemAvailable/{printf \"%d\\n\", $2 * 0.01*{{percentage}};}' < /proc/meminfo)k --vm-keep -m 1 -t {{timeout}}</p>\n<p><a href=\"https://cloud.tencent.com/document/api/1340/52676\">tat官方文档</a></p>\n<p><a href=\"https://wiki.ubuntu.com/Kernel/Reference/stress-ng\">stress-ng官方文档</a></p>",
                "ResourceType": "内存资源",
                "IsAllowed": true,
                "ActionBestCase": "",
                "ObjectType": "CVM",
                "MetricIdList": []
            },
            {
                "ActionName": "磁盘分区使用率高",
                "Desc": "使用stress-ng压测工具压测，支持的linux发行版：Centos7.2及以上，CoreOS 1745.5.0及以上，Debian9.0及以上，Ubuntu 16.04.1及以上",
                "ActionType": "平台",
                "CreateTime": "2022-11-29 18:08:46",
                "Creator": "系统",
                "UpdateTime": "2022-11-29 18:08:46",
                "RiskDesc": "高风险",
                "ActionId": 8,
                "AttributeId": 1,
                "RelationActionId": 0,
                "ActionCommand": "#!/bin/bash\n\nuser=$(whoami)\nif [ !$user == 'root' ]\nthen\n    sudo -i\nfi\n\nfunction command_exists(){\n    if command -v $1 > /dev/null 2>&1; then\n        return 1\n    else\n        return 0\n    fi\n}\n\necho -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\n\nos_desc=$(cat /etc/*release)\n# echo $os_desc\n\ndeclare -A os_dic\nos_dic=([CentOS]=\"yum install stress-ng -y\" \\\n        [CoreOS]=\"docker pull alexeiled/stress-ng\" \\\n        [Debian]=\"apt-get install -y stress-ng\" \\\n        [Ubuntu]=\"apt-get install -y stress-ng\")\n\nos_name='N/A'\n\nfor key in $(echo ${!os_dic[*]})\ndo\n    if [[ $os_desc =~ $key ]]\n    then\n        os_name=$key\n        echo $key\n    fi\ndone\n\nif [ $os_name == 'N/A' ]\nthen\n    echo \"Unsupported Linux distributions\"\n    exit 1\nfi\n\n# os_name=$(cat /etc/*release | awk 'NR==1{print($1)}')\n\necho -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\necho \"installing stress-ng...\"\ncommand_exists stress-ng\n\nif [[ $? -eq 0 ]]\nthen\n    ${os_dic[$os_name]}\n    echo -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\n    echo \"Checking the installation status...\"\n    command_exists stress-ng\n    if [[ $? -eq 0 && $os_name != 'CoreOS' ]]\n    then\n        echo -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\n        echo \"Fail to install\"\n        exit 1\n    else\n        echo -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\n        echo \"stress-ng has already installed\"\n    fi\nelse\n    echo -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\n    echo \"stress-ng has already installed\"\nfi\n\necho -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\necho \"Starting to perform stress test.\"\nif [ $os_name == \"CoreOS\" ]\nthen\n    cd {{dir}} && docker run --rm alexeiled/stress-ng --iomix 1 --iomix-bytes  `df -k {{dir}} | awk 'NR==2{printf(\"%d\\n\", ($3+$4)*0.01*{{percentage}}-$3)}'`k -t {{timeout}}\nelse\n    cd {{dir}} && stress-ng --iomix 1 --iomix-bytes  `df -k {{dir}} | awk 'NR==2{printf(\"%d\\n\", ($3+$4)*0.01*{{percentage}}-$3)}'`k -t {{timeout}}\nfi\n\nif [[ !$? -eq 0 ]]\nthen\n    echo -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\n    echo \"Failed\"\n    exit 1\nelse\n    echo -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\n    echo \"Completed\"\n    exit 0\nfi",
                "ActionContent": "#!/bin/bash\n\nuser=$(whoami)\nif [ !$user == 'root' ]\nthen\n    sudo -i\nfi\n\nfunction command_exists(){\n    if command -v $1 > /dev/null 2>&1; then\n        return 1\n    else\n        return 0\n    fi\n}\n\necho -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\n\nos_desc=$(cat /etc/*release)\n# echo $os_desc\n\ndeclare -A os_dic\nos_dic=([CentOS]=\"yum install stress-ng -y\" \\\n        [CoreOS]=\"docker pull alexeiled/stress-ng\" \\\n        [Debian]=\"apt-get install -y stress-ng\" \\\n        [Ubuntu]=\"apt-get install -y stress-ng\")\n\nos_name='N/A'\n\nfor key in $(echo ${!os_dic[*]})\ndo\n    if [[ $os_desc =~ $key ]]\n    then\n        os_name=$key\n        echo $key\n    fi\ndone\n\nif [ $os_name == 'N/A' ]\nthen\n    echo \"Unsupported Linux distributions\"\n    exit 1\nfi\n\n# os_name=$(cat /etc/*release | awk 'NR==1{print($1)}')\n\necho -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\necho \"installing stress-ng...\"\ncommand_exists stress-ng\n\nif [[ $? -eq 0 ]]\nthen\n    ${os_dic[$os_name]}\n    echo -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\n    echo \"Checking the installation status...\"\n    command_exists stress-ng\n    if [[ $? -eq 0 && $os_name != 'CoreOS' ]]\n    then\n        echo -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\n        echo \"Fail to install\"\n        exit 1\n    else\n        echo -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\n        echo \"stress-ng has already installed\"\n    fi\nelse\n    echo -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\n    echo \"stress-ng has already installed\"\nfi\n\necho -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\necho \"Starting to perform stress test.\"\nif [ $os_name == \"CoreOS\" ]\nthen\n    cd {{dir}} && docker run --rm alexeiled/stress-ng --iomix 1 --iomix-bytes  `df -k {{dir}} | awk 'NR==2{printf(\"%d\\n\", ($3+$4)*0.01*{{percentage}}-$3)}'`k -t {{timeout}}\nelse\n    cd {{dir}} && stress-ng --iomix 1 --iomix-bytes  `df -k {{dir}} | awk 'NR==2{printf(\"%d\\n\", ($3+$4)*0.01*{{percentage}}-$3)}'`k -t {{timeout}}\nfi\n\nif [[ !$? -eq 0 ]]\nthen\n    echo -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\n    echo \"Failed\"\n    exit 1\nelse\n    echo -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\n    echo \"Completed\"\n    exit 0\nfi",
                "ActionCommandType": 0,
                "ActionDetail": "<p>使用tat通道下发stress-ng命令进行压测</p>\n<p>命令内容：stress-ng --iomix 1 --iomix-bytes  `df -k {{dir}} | awk 'NR==2{printf(\"%d\\n\", ($3+$4)*0.01*{{percentage}}-$3)}'`k -t {{timeout}}</p>\n<p><a href=\"https://cloud.tencent.com/document/api/1340/52676\">tat官方文档</a></p>\n<p><a href=\"https://wiki.ubuntu.com/Kernel/Reference/stress-ng\">stress-ng官方文档</a></p>\n",
                "ResourceType": "磁盘资源",
                "IsAllowed": true,
                "ActionBestCase": "",
                "ObjectType": "CVM",
                "MetricIdList": []
            },
            {
                "ActionName": "内核故障",
                "Desc": "会触发实例重启",
                "ActionType": "平台",
                "CreateTime": "2022-11-29 18:08:46",
                "Creator": "系统",
                "UpdateTime": "2022-11-29 18:08:46",
                "RiskDesc": "高风险",
                "ActionId": 9,
                "AttributeId": 1,
                "RelationActionId": 24,
                "ActionCommand": "echo -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\" && echo 'inject kernel error success!' && echo -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\" && sleep 5 && echo -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\" && echo c > /proc/sysrq-trigger &",
                "ActionContent": "echo -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\" && echo 'inject kernel error success!' && echo -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\" && sleep 5 && echo -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\" && echo c > /proc/sysrq-trigger &",
                "ActionCommandType": 0,
                "ActionDetail": "<p>使用tat通道下发内核故障命令</p>\n<p>命令内容：echo c > /proc/sysrq-trigger</p>\n<p><a href=\"https://cloud.tencent.com/document/api/1340/52676\">tat官方文档</a></p>",
                "ResourceType": "CPU资源",
                "IsAllowed": true,
                "ActionBestCase": "",
                "ObjectType": "CVM",
                "MetricIdList": []
            },
            {
                "ActionName": "磁盘IO负载",
                "Desc": "使用stress-ng压测工具压测，支持的linux发行版：Centos7.2及以上，CoreOS 1745.5.0及以上，Debian9.0及以上，Ubuntu 16.04.1及以上",
                "ActionType": "平台",
                "CreateTime": "2022-11-29 18:08:46",
                "Creator": "系统",
                "UpdateTime": "2022-11-29 18:08:46",
                "RiskDesc": "高风险",
                "ActionId": 10,
                "AttributeId": 1,
                "RelationActionId": 0,
                "ActionCommand": "#!/bin/bash\n\nuser=$(whoami)\nif [ !$user == 'root' ]\nthen\n    sudo -i\nfi\n\nfunction command_exists(){\n    if command -v $1 > /dev/null 2>&1; then\n        return 1\n    else\n        return 0\n    fi\n}\n\necho -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\n\nos_desc=$(cat /etc/*release)\n# echo $os_desc\n\ndeclare -A os_dic\nos_dic=([CentOS]=\"yum install stress-ng -y\" \\\n        [CoreOS]=\"docker pull alexeiled/stress-ng\" \\\n        [Debian]=\"apt-get install -y stress-ng\" \\\n        [Ubuntu]=\"apt-get install -y stress-ng\")\n\nos_name='N/A'\n\nfor key in $(echo ${!os_dic[*]})\ndo\n    if [[ $os_desc =~ $key ]]\n    then\n        os_name=$key\n        echo $key\n    fi\ndone\n\nif [ $os_name == 'N/A' ]\nthen\n    echo \"Unsupported Linux distributions\"\n    exit 1\nfi\n\n# os_name=$(cat /etc/*release | awk 'NR==1{print($1)}')\n\necho -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\necho \"installing stress-ng...\"\ncommand_exists stress-ng\n\nif [[ $? -eq 0 ]]\nthen\n    ${os_dic[$os_name]}\n    echo -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\n    echo \"Checking the installation status...\"\n    command_exists stress-ng\n    if [[ $? -eq 0 && $os_name != 'CoreOS' ]]\n    then\n        echo -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\n        echo \"Fail to install\"\n        exit 1\n    else\n        echo -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\n        echo \"stress-ng has already installed\"\n    fi\nelse\n    echo -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\n    echo \"stress-ng has already installed\"\nfi\n\necho -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\necho \"Starting to perform stress test.\"\nif [ $os_name == \"CoreOS\" ]\nthen\n    docker run --rm alexeiled/stress-ng --vm-bytes {{bytes_num}}{{bytes_unit}} --hdd {{io_process_num}} --vm-keep -t {{timeout}}\nelse\n    stress-ng --vm-bytes {{bytes_num}}{{bytes_unit}} --hdd {{io_process_num}} --vm-keep -t {{timeout}}\nfi\n\nif [[ !$? -eq 0 ]]\nthen\n    echo -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\n    echo \"Failed\"\n    exit 1\nelse\n    echo -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\n    echo \"Completed\"\n    exit 0\nfi",
                "ActionContent": "#!/bin/bash\n\nuser=$(whoami)\nif [ !$user == 'root' ]\nthen\n    sudo -i\nfi\n\nfunction command_exists(){\n    if command -v $1 > /dev/null 2>&1; then\n        return 1\n    else\n        return 0\n    fi\n}\n\necho -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\n\nos_desc=$(cat /etc/*release)\n# echo $os_desc\n\ndeclare -A os_dic\nos_dic=([CentOS]=\"yum install stress-ng -y\" \\\n        [CoreOS]=\"docker pull alexeiled/stress-ng\" \\\n        [Debian]=\"apt-get install -y stress-ng\" \\\n        [Ubuntu]=\"apt-get install -y stress-ng\")\n\nos_name='N/A'\n\nfor key in $(echo ${!os_dic[*]})\ndo\n    if [[ $os_desc =~ $key ]]\n    then\n        os_name=$key\n        echo $key\n    fi\ndone\n\nif [ $os_name == 'N/A' ]\nthen\n    echo \"Unsupported Linux distributions\"\n    exit 1\nfi\n\n# os_name=$(cat /etc/*release | awk 'NR==1{print($1)}')\n\necho -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\necho \"installing stress-ng...\"\ncommand_exists stress-ng\n\nif [[ $? -eq 0 ]]\nthen\n    ${os_dic[$os_name]}\n    echo -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\n    echo \"Checking the installation status...\"\n    command_exists stress-ng\n    if [[ $? -eq 0 && $os_name != 'CoreOS' ]]\n    then\n        echo -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\n        echo \"Fail to install\"\n        exit 1\n    else\n        echo -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\n        echo \"stress-ng has already installed\"\n    fi\nelse\n    echo -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\n    echo \"stress-ng has already installed\"\nfi\n\necho -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\necho \"Starting to perform stress test.\"\nif [ $os_name == \"CoreOS\" ]\nthen\n    docker run --rm alexeiled/stress-ng --vm-bytes {{bytes_num}}{{bytes_unit}} --hdd {{io_process_num}} --vm-keep -t {{timeout}}\nelse\n    stress-ng --vm-bytes {{bytes_num}}{{bytes_unit}} --hdd {{io_process_num}} --vm-keep -t {{timeout}}\nfi\n\nif [[ !$? -eq 0 ]]\nthen\n    echo -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\n    echo \"Failed\"\n    exit 1\nelse\n    echo -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\n    echo \"Completed\"\n    exit 0\nfi",
                "ActionCommandType": 0,
                "ActionDetail": "<p>使用tat通道下发stress-ng命令进行压测</p>\n<p>命令内容：stress-ng --vm-bytes {{bytes_num}}{{bytes_unit}} --hdd {{io_process_num}} --vm-keep -t {{timeout}}</p>\n<p><a href=\"https://cloud.tencent.com/document/api/1340/52676\">tat官方文档</a></p>",
                "ResourceType": "IO资源",
                "IsAllowed": true,
                "ActionBestCase": "",
                "ObjectType": "CVM",
                "MetricIdList": []
            },
            {
                "ActionName": "内存OOM",
                "Desc": "使用stress-ng压测工具压测，支持的linux发行版：Centos7.2及以上，CoreOS 1745.5.0及以上，Debian9.0及以上，Ubuntu 16.04.1及以上",
                "ActionType": "平台",
                "CreateTime": "2023-07-04 11:20:43",
                "Creator": "系统",
                "UpdateTime": "2023-07-04 11:20:43",
                "RiskDesc": "高风险",
                "ActionId": 11,
                "AttributeId": 1,
                "RelationActionId": 0,
                "ActionCommand": "#!/bin/bash\n\nuser=$(whoami)\nif [ !$user == 'root' ]\nthen\n    sudo -i\nfi\n\nfunction command_exists(){\n    if command -v $1 > /dev/null 2>&1; then\n        return 1\n    else\n        return 0\n    fi\n}\n\necho -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\n\nos_desc=$(cat /etc/*release)\n# echo $os_desc\n\ndeclare -A os_dic\nos_dic=([CentOS]=\"yum install stress-ng -y\" \\\n        [CoreOS]=\"docker pull alexeiled/stress-ng\" \\\n        [Debian]=\"apt-get install -y stress-ng\" \\\n        [Ubuntu]=\"apt-get install -y stress-ng\")\n\nos_name='N/A'\n\nfor key in $(echo ${!os_dic[*]})\ndo\n    if [[ $os_desc =~ $key ]]\n    then\n        os_name=$key\n        echo $key\n    fi\ndone\n\nif [ $os_name == 'N/A' ]\nthen\n    echo \"Unsupported Linux distributions\"\n    exit 1\nfi\n\n# os_name=$(cat /etc/*release | awk 'NR==1{print($1)}')\n\necho -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\necho \"installing stress-ng...\"\ncommand_exists stress-ng\n\nif [[ $? -eq 0 ]]\nthen\n    ${os_dic[$os_name]}\n    echo -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\n    echo \"Checking the installation status...\"\n    command_exists stress-ng\n    if [[ $? -eq 0 && $os_name != 'CoreOS' ]]\n    then\n        echo -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\n        echo \"Fail to install\"\n        exit 1\n    else\n        echo -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\n        echo \"stress-ng has already installed\"\n    fi\nelse\n    echo -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\n    echo \"stress-ng has already installed\"\nfi\n\necho -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\necho \"Starting to perform stress test.\"\nif [ $os_name == \"CoreOS\" ]\nthen\n    docker run --rm alexeiled/stress-ng --bigheap 10 --bigheap-growth 4K -t {{timeout}}\nelse\n    stress-ng --bigheap 10 --bigheap-growth 4K -t {{timeout}}\nfi\necho \"Completed\"\n\n",
                "ActionContent": "#!/bin/bash\n\nuser=$(whoami)\nif [ !$user == 'root' ]\nthen\n    sudo -i\nfi\n\nfunction command_exists(){\n    if command -v $1 > /dev/null 2>&1; then\n        return 1\n    else\n        return 0\n    fi\n}\n\necho -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\n\nos_desc=$(cat /etc/*release)\n# echo $os_desc\n\ndeclare -A os_dic\nos_dic=([CentOS]=\"yum install stress-ng -y\" \\\n        [CoreOS]=\"docker pull alexeiled/stress-ng\" \\\n        [Debian]=\"apt-get install -y stress-ng\" \\\n        [Ubuntu]=\"apt-get install -y stress-ng\")\n\nos_name='N/A'\n\nfor key in $(echo ${!os_dic[*]})\ndo\n    if [[ $os_desc =~ $key ]]\n    then\n        os_name=$key\n        echo $key\n    fi\ndone\n\nif [ $os_name == 'N/A' ]\nthen\n    echo \"Unsupported Linux distributions\"\n    exit 1\nfi\n\n# os_name=$(cat /etc/*release | awk 'NR==1{print($1)}')\n\necho -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\necho \"installing stress-ng...\"\ncommand_exists stress-ng\n\nif [[ $? -eq 0 ]]\nthen\n    ${os_dic[$os_name]}\n    echo -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\n    echo \"Checking the installation status...\"\n    command_exists stress-ng\n    if [[ $? -eq 0 && $os_name != 'CoreOS' ]]\n    then\n        echo -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\n        echo \"Fail to install\"\n        exit 1\n    else\n        echo -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\n        echo \"stress-ng has already installed\"\n    fi\nelse\n    echo -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\n    echo \"stress-ng has already installed\"\nfi\n\necho -e \"[\"`date +\"%Y-%m-%d %H:%M:%S\"`\"] \\c\"\necho \"Starting to perform stress test.\"\nif [ $os_name == \"CoreOS\" ]\nthen\n    docker run --rm alexeiled/stress-ng --bigheap 10 --bigheap-growth 4K -t {{timeout}}\nelse\n    stress-ng --bigheap 10 --bigheap-growth 4K -t {{timeout}}\nfi\necho \"Completed\"\n\n",
                "ActionCommandType": 0,
                "ActionDetail": "<p>使用tat通道下发stress-ng命令进行压测</p>\n<p>命令内容：stress-ng --bigheap 10 --bigheap-growth 4K -t {{timeout}}</p>\n<p><a href=\"https://cloud.tencent.com/document/api/1340/52676\">tat官方文档</a></p>",
                "ResourceType": "内存资源",
                "IsAllowed": true,
                "ActionBestCase": "https://cloud.tencent.com/document/product/1500/81504",
                "ObjectType": "CVM",
                "MetricIdList": []
            },
            {
                "ActionName": "空操作",
                "Desc": "空操作，用于测试流程，不做实际注入操作",
                "ActionType": "平台",
                "CreateTime": "2022-11-29 18:08:46",
                "Creator": "系统",
                "UpdateTime": "2022-11-29 18:08:46",
                "RiskDesc": "低风险",
                "ActionId": 12,
                "AttributeId": 1,
                "RelationActionId": 13,
                "ActionCommand": "调用腾讯云对应产品的API接口",
                "ActionContent": "空操作",
                "ActionCommandType": 1,
                "ActionDetail": null,
                "ResourceType": "其他",
                "IsAllowed": true,
                "ActionBestCase": "",
                "ObjectType": "CVM",
                "MetricIdList": []
            }
        ],
        "Total": 45
    }
}
```

