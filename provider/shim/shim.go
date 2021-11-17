package shim

import (
	"github.com/hashicorp/terraform-plugin-sdk/v2/helper/schema"
	"github.com/hashicorp/terraform-provider-time/internal/tftime"
)

func NewProvider() *schema.Provider {
	return tftime.Provider()
}
