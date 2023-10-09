package shim

import (
	"github.com/hashicorp/terraform-provider-time/internal/provider"
	tf "github.com/hashicorp/terraform-plugin-framework/provider"
)

func NewProvider() tf.Provider {
		return provider.New()
}
