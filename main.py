#!/usr/local/bin/python2
# should be brew python with latest openssl

import os
import json
import sys
from functools import partial
from lib.workflow import Workflow3
from lib.asana import Client

REQUIRED_ENV_VARIABLES = ['ASANA_PERSONAL_TOKEN', 'ASANA_WORKSPACE_NAME', 'ASANA_PROJECT_NAME']


def get_workspace_by_name(client, name):
  workspaces = client.workspaces.find_all()
  return next((workspace for workspace in workspaces if workspace.get('name') == name), None)


def get_project_by_name(client, workspace_id, name):
  projects = client.projects.find_by_workspace(workspace_id)
  return next((project for project in projects if project.get('name') == name), None)


def get_me(client):
  return client.users.me()


def main(wf):
  if any(variable not in os.environ for variable in REQUIRED_ENV_VARIABLES) or not wf.args:
    exit(1)

  client = Client.access_token(os.getenv('ASANA_PERSONAL_TOKEN'))

  workspace = wf.cached_data('workspace', partial(get_workspace_by_name, client, os.getenv('ASANA_WORKSPACE_NAME')), max_age=604800)

  if not workspace:
    raise Exception('Workspace was not found')

  project = wf.cached_data('project', partial(get_project_by_name, client, workspace.get('id'), os.getenv('ASANA_PROJECT_NAME')), max_age=604800)

  if not project:
    raise Exception('Project was not found in the workspace')

  me = wf.cached_data('me', partial(get_me, client), max_age=604800)

  result = client.tasks.create_in_workspace(workspace.get('id'), {
    'name': wf.args[0],
    'assignee': me.get('id'),
    'projects': [project.get('id')],
  })

  return result.get('id')


if __name__ == "__main__":
  wf = Workflow3()
  sys.exit(wf.run(main))
