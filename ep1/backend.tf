terraform{
    required_version = "~>1.5"
    backend gcs{
        bucket="ranjana-state"
        prefix = "terraform/ep1"
    }
}
provider "google" {
  
}