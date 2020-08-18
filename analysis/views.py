from django.views.generic import FormView
from django.urls import reverse_lazy
from . import forms as analysis_forms
from . import models


class BitcoinView(FormView):
    form_class = analysis_forms.BotForm
    success_url = reverse_lazy('success')
    template_name = 'analysis/bitcoin.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        code = 'Bitcoin'
        date = '2020-07-28'
        hour = '09'

        if self.request.GET.get('code', None):
            code = self.request.GET.get('code', None)
        if self.request.GET.get('date', None):
            date = self.request.GET.get('date', None)
        if self.request.GET.get('hour', None):
            hour = self.request.GET.get('hour', None)
        start_date = date + ' ' + hour + ':00:00'

        context['date_list'] = models.TickerDate.objects.raw(
            'SELECT max(tcsn) as id, substr(adddate(adddate(tcStartTime, INTERVAL 9 HOUR), INTERVAL -%s HOUR), 1, 11) '
            + 'as ticker_date FROM tTicker GROUP BY ticker_date ORDER BY ticker_date', [hour])
        context['ticker_5_list'] = models.Ticker.objects.raw(
            'SELECT tcsn as id, tcItemCode as code, adddate(tcStartTime, INTERVAL 9 HOUR) as start_time, '
            + 'tcOpenPrice as open_price, tcStatus as status FROM tTicker '
            + 'WHERE tcItemCode=%s and tcTimeScale=%s and adddate(tcStartTime, INTERVAL 9 HOUR) >= %s and '
            + 'adddate(tcStartTime, INTERVAL -15 HOUR) < %s order by start_time desc'
            , [code, 5, start_date, start_date])
        context['ticker_3_list'] = models.Ticker.objects.raw(
            'SELECT tcsn as id, tcItemCode as code, adddate(tcStartTime, INTERVAL 9 HOUR) as start_time, '
            + 'tcOpenPrice as open_price, tcStatus as status FROM tTicker '
            + 'WHERE tcItemCode=%s and tcTimeScale=%s and adddate(tcStartTime, INTERVAL 9 HOUR) >= %s and '
            + 'adddate(tcStartTime, INTERVAL -15 HOUR) < %s order by start_time desc'
            , [code, 3, start_date, start_date])
        context['ticker_2_list'] = models.Ticker.objects.raw(
            'SELECT tcsn as id, tcItemCode as code, adddate(tcStartTime, INTERVAL 9 HOUR) as start_time, '
            + 'tcOpenPrice as open_price, tcStatus as status FROM tTicker '
            + 'WHERE tcItemCode=%s and tcTimeScale=%s and adddate(tcStartTime, INTERVAL 9 HOUR) >= %s and '
            + 'adddate(tcStartTime, INTERVAL -15 HOUR) < %s order by start_time desc'
            , [code, 2, start_date, start_date])
        context['ticker_1_list'] = models.Ticker.objects.raw(
            'SELECT tcsn as id, tcItemCode as code, adddate(tcStartTime, INTERVAL 9 HOUR) as start_time, '
            + 'tcOpenPrice as open_price, tcStatus as status FROM tTicker '
            + 'WHERE tcItemCode=%s and tcTimeScale=%s and adddate(tcStartTime, INTERVAL 9 HOUR) >= %s and '
            + 'adddate(tcStartTime, INTERVAL -15 HOUR) < %s order by start_time desc'
            , [code, 1, start_date, start_date])
        return context


class ChartView(FormView):
    form_class = analysis_forms.BotForm
    success_url = reverse_lazy('success')
    template_name = 'analysis/chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        code = 'Bitcoin'
        date = '2020-06-24'
        hour = '09'

        if self.request.GET.get('code', None):
            code = self.request.GET.get('code', None)
        if self.request.GET.get('date', None):
            date = self.request.GET.get('date', None)
        if self.request.GET.get('hour', None):
            hour = self.request.GET.get('hour', None)
        start_date = date + ' ' + hour + ':00:00'

        context['date_list'] = models.TickerDate.objects.raw(
            'SELECT max(tcsn) as id, substr(adddate(adddate(tcStartTime, INTERVAL 9 HOUR), INTERVAL -%s HOUR), 1, 11) '
            + 'as ticker_date FROM tTicker GROUP BY ticker_date ORDER BY ticker_date', [hour])
        context['ticker_5_list'] = models.Ticker.objects.raw(
            'SELECT tcsn as id, tcItemCode as code, adddate(tcStartTime, INTERVAL 9 HOUR) as start_time, '
            + 'tcOpenPrice as open_price, tcStatus as status FROM tTicker '
            + 'WHERE tcItemCode=%s and tcTimeScale=%s and adddate(tcStartTime, INTERVAL 9 HOUR) >= %s and '
            + 'adddate(tcStartTime, INTERVAL -15 HOUR) < %s order by start_time desc'
            , [code, 5, start_date, start_date])
        context['ticker_3_list'] = models.Ticker.objects.raw(
            'SELECT tcsn as id, tcItemCode as code, adddate(tcStartTime, INTERVAL 9 HOUR) as start_time, '
            + 'tcOpenPrice as open_price, tcStatus as status FROM tTicker '
            + 'WHERE tcItemCode=%s and tcTimeScale=%s and adddate(tcStartTime, INTERVAL 9 HOUR) >= %s and '
            + 'adddate(tcStartTime, INTERVAL -15 HOUR) < %s order by start_time desc'
            , [code, 3, start_date, start_date])
        context['ticker_2_list'] = models.Ticker.objects.raw(
            'SELECT tcsn as id, tcItemCode as code, adddate(tcStartTime, INTERVAL 9 HOUR) as start_time, '
            + 'tcOpenPrice as open_price, tcStatus as status FROM tTicker '
            + 'WHERE tcItemCode=%s and tcTimeScale=%s and adddate(tcStartTime, INTERVAL 9 HOUR) >= %s and '
            + 'adddate(tcStartTime, INTERVAL -15 HOUR) < %s order by start_time desc'
            , [code, 2, start_date, start_date])
        context['ticker_1_list'] = models.Ticker.objects.raw(
            'SELECT tcsn as id, tcItemCode as code, adddate(tcStartTime, INTERVAL 9 HOUR) as start_time, '
            + 'tcOpenPrice as open_price, tcStatus as status FROM tTicker '
            + 'WHERE tcItemCode=%s and tcTimeScale=%s and adddate(tcStartTime, INTERVAL 9 HOUR) >= %s and '
            + 'adddate(tcStartTime, INTERVAL -15 HOUR) < %s order by start_time desc'
            , [code, 1, start_date, start_date])
        return context


class ListView(FormView):
    form_class = analysis_forms.BotForm
    success_url = reverse_lazy('success')
    template_name = 'analysis/list.html'

    form_class.date = models.TickerDate.objects.raw(
        'select substr(adddate(tcStartTime, INTERVAL %s HOUR), 1, 11) as date from tTicker group by ticker_date '
        + 'order by ticker_date desc')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        code = 'Bitcoin'
        date = '2020-06-29'
        hour = '00'

        if self.request.GET.get('code', None):
            code = self.request.GET.get('code', None)
        if self.request.GET.get('date', None):
            date = self.request.GET.get('date', None)
        if self.request.GET.get('hour', None):
            hour = self.request.GET.get('hour', None)
        start_date = date + ' ' + hour + ':00:00'

        # context['date_list'] = models.TickerDate.objects.raw(
        #     'SELECT substr(adddate(tcStartTime, INTERVAL %s HOUR), 1, 11) as ticker_date FROM tTicker '
        #     + 'GROUP BY ticker_date ORDER BY ticker_date DESC', [hour])

        context['date_list'] = models.TickerDate.objects.raw(
            'SELECT substr(adddate(tcStartTime, INTERVAL %s HOUR), 1, 11) as ticker_date '
            + 'FROM tTicker GROUP BY ticker_date ORDER BY ticker_date DESC', [hour])

        context['ticker_5_list'] = models.Ticker.objects.raw(
            'SELECT tcsn as id, tcItemCode as code, adddate(tcStartTime, INTERVAL 9 HOUR) as start_time, '
            + 'tcOpenPrice as open_price, tcStatus as status FROM tTicker '
            + 'WHERE tcItemCode=%s and tcTimeScale=%s and adddate(tcStartTime, INTERVAL 9 HOUR) >= %s and '
            + 'adddate(tcStartTime, INTERVAL -15 HOUR) < %s order by start_time desc'
            , [code, 5, start_date, start_date])
        context['ticker_3_list'] = models.Ticker.objects.raw(
            'SELECT tcsn as id, tcItemCode as code, adddate(tcStartTime, INTERVAL 9 HOUR) as start_time, '
            + 'tcOpenPrice as open_price, tcStatus as status FROM tTicker '
            + 'WHERE tcItemCode=%s and tcTimeScale=%s and adddate(tcStartTime, INTERVAL 9 HOUR) >= %s and '
            + 'adddate(tcStartTime, INTERVAL -15 HOUR) < %s order by start_time desc'
            , [code, 3, start_date, start_date])
        context['ticker_2_list'] = models.Ticker.objects.raw(
            'SELECT tcsn as id, tcItemCode as code, adddate(tcStartTime, INTERVAL 9 HOUR) as start_time, '
            + 'tcOpenPrice as open_price, tcStatus as status FROM tTicker '
            + 'WHERE tcItemCode=%s and tcTimeScale=%s and adddate(tcStartTime, INTERVAL 9 HOUR) >= %s and '
            + 'adddate(tcStartTime, INTERVAL -15 HOUR) < %s order by start_time desc'
            , [code, 2, start_date, start_date])
        context['ticker_1_list'] = models.Ticker.objects.raw(
            'SELECT tcsn as id, tcItemCode as code, adddate(tcStartTime, INTERVAL 9 HOUR) as start_time, '
            + 'tcOpenPrice as open_price, tcStatus as status FROM tTicker '
            + 'WHERE tcItemCode=%s and tcTimeScale=%s and adddate(tcStartTime, INTERVAL 9 HOUR) >= %s and '
            + 'adddate(tcStartTime, INTERVAL -15 HOUR) < %s order by start_time desc'
            , [code, 1, start_date, start_date])
        return context
