class compute:

    def vm_list(self, project_id):

        from gcp_project_deletion.variable import service

        vm_exist = False

        zone_request = service.zones().list(project=project_id)

        zone_response = zone_request.execute()

        for zone_details in zone_response['items']:

            zone_name = zone_details.get("name")

            instance_request = service.instances().list(project=project_id, zone=zone_name)

            instance_response = instance_request.execute()

            instance_details = instance_response.get("items", "")

            if len(instance_details) > 0:

                vm_exist = True

                break

        if vm_exist:

            print("Instances exists in project please delete")

        else:

            print("Instances doesn't exists in the project")

        return vm_exist
