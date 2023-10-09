package shim

import (
	tf "github.com/hashicorp/terraform-plugin-framework/provider"
	"github.com/hashicorp/terraform-provider-time/internal/provider"
)

func NewProvider() tf.Provider {
	return provider.New()
}
