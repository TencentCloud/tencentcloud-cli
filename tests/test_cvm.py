from utils import shell


def test_describe_regions():
    assert "\"Region\": \"ap-guangzhou\"" in shell("tccli cvm DescribeRegions")


def test_describe_instances():
    assert "\"TotalCount\":" in shell("tccli cvm DescribeInstances")


def test_describe_disaster_disaster_recover_group_quota():
    assert "\"CvmInHostGroupQuota\":" in shell("tccli cvm DescribeDisasterRecoverGroupQuota")


def test_describe_disaster_recover_groups():
    assert "DisasterRecoverGroupSet" in shell("tccli cvm DescribeDisasterRecoverGroups")


def test_describe_hosts():
    cmd = 'tccli cvm DescribeHosts --cli-unfold-argument'
    cmd += ' --Filters.0.Name zone'
    cmd += ' --Filters.0.Values ap-guangzhou-2'
    cmd += ' --Offset 0 --Limit 20'

    assert "\"HostSet\": []" in shell(cmd)
