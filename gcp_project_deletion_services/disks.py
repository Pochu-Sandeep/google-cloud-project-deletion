class disks:

    def disks_list(self, project_id):

        from gcp_project_deletion_services.variable import service

        zone_request = service.zones().list(project=project_id)

        zone_response = zone_request.execute()

        for zone_details in zone_response['items']:

            zone_name = zone_details.get("name")

            disks_request = service.disks().list(project=project_id, zone=zone_name)

            disks_response = disks_request.execute()

            disk_details = disks_response.get("items", "")

            if len(disk_details) > 0:

                disks_exist = True

                disk_name_list = [sub['name'] for sub in disk_details]

                print(disk_name_list)

                for disk_name in disk_name_list:

                    print(disk_name)

                    disk_delete_request = service.disks().delete(project=project_id, zone=zone_name, disk=disk_name)

                    print("disk "+disk_name+" from zone "+zone_name+" of project "+project_id+" is now getting deleted")

                    disk_delete_response = disk_delete_request.execute()

            else:

                disks_exist = False

        return disks_exist

