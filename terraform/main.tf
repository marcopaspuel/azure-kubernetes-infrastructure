provider "azurerm" {
    # NOTE: to get around registering all kinds of providers
    skip_provider_registration = true

    features {}
}

terraform {
    required_providers {
      azurerm = {
        source  = "hashicorp/azurerm"
        version = ">= 2.0"
      }
    }
    backend "azurerm" {}
}
