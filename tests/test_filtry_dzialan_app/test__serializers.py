import pytest
import factory

from rest_framework.fields import CharField

from apps.transaction.api.serializers import CurrencySerializer, UnfilledTransactionSerializer, FilledTransactionSerializer
from tests.test_transaction.factories import CurrencyFactory, UnfilledTransactionFactory, FilledTransactionFactory
