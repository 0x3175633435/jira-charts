from jira import JIRA
from insights import IssueTypes, Assignee

username = input("username: ")
password = input("password: ")

jira = JIRA("https://bevicred.atlassian.net", auth=(username, password))
list = jira.search_issues("project = ERP AND status = Done")

IssueTypes.organize(list)
Assignee.organize(list)