from dal import autocomplete

from api.models import Country,Object

class ObjectAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Object.objects.none()

        qs = Object.objects.all()

        country = self.forwarded.get('country', None)

        if country:
            qs = qs.filter(country=country)
        if self.q:
            qs = qs.filter(name__istartswith=self.q)
        return qs