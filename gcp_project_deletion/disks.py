class disks:

    def disks_list(self, project_id):

        disks_exist = False

        from gcp_project_deletion.variable import service

        zone_request = service.zones().list(project=project_id)

        zone_response = zone_request.execute()

        for zone_details in zone_response['items']:

            zone_name = zone_details.get("name")

            disks_request = service.disks().list(project=project_id, zone=zone_name)

            disks_response = disks_request.execute()

            disk_details = disks_response.get("items", "")

            if len(disk_details) > 0:

                disks_exist = True

                break

        if disks_exist:

            print("Disks exists in project please delete")

        else:

            print("Disks doesn't exists in the project")

        return disks_exist