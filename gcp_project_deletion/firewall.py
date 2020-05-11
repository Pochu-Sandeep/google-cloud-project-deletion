class firewall:

    def firewall_list(self, project_id):

        firewall_exist = False

        from gcp_project_deletion.variable import service

        firewall_request = service.firewalls().list(project=project_id)

        firewall_response = firewall_request.execute()

        firewall_details = firewall_response.get("items", "")

        if len(firewall_details) > 0:

            firewall_exist = True

            print("Firewalls exists in project, please delete")

        else:

            print("Firewalls doesn't exist in the project")

        return firewall_exist