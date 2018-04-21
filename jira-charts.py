from jira import JIRA
from insights import IssueTypes, Assignee
from getpass import getpass

username = input("Username: ")
password = input("Password: ")

jira = JIRA("https://bevicred.atlassian.net", auth=(username, password))
list = jira.search_issues("project = ERP AND status = Done AND fixVersion = v1.2.0", maxResults = False)

IssueTypes.organize(list)
Assignee.organize(list)