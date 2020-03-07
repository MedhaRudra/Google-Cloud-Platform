class MyConfiguration():

    #setting the configuration of vm instance
    def setconfig():
        config = {
            "machineType": "zones/us-central1-a/machineTypes/n1-standard-1",
            "disks":
            [
                {
                    "boot": "True",
                    "initializeParams": {"sourceImage": "projects/debian-cloud/global/images/family/debian-9"}
                }
            ],
            "networkInterfaces": [{"network": "global/networks/default"}]
        }
        return config
    
    def myinput():
        
        project_name="qwiklabs-gcp-00-832737805b5c"
        zone_name="us-central1-a"
        no_of_vm="2"
        
        return no_of_vm, project_name, zone_name
		
