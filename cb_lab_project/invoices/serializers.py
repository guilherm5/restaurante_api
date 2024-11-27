from rest_framework import serializers
from .models import DetailLine, GuestCheck, MenuItem

class DetailLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailLine
        fields = '__all__'
        
class GuestCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuestCheck
        fields = '__all__'

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['menu_item_id', 'mod_flag', 'incl_tax', 'active_taxes', 'prc_lvl']

class DetailLineSerializer(serializers.ModelSerializer):
    menu_item = MenuItemSerializer()  

    class Meta:
        model = DetailLine
        fields = [
            'guest_check_line_item_id', 'guest_check_id', 'rvc_num', 'dtl_ot_num', 'dtl_oc_num', 'line_num', 
            'dtl_id', 'detail_utc', 'detail_lcl', 'last_update_utc', 'last_update_lcl', 'bus_dt', 
            'ws_num', 'dsp_ttl', 'dsp_qty', 'agg_ttl', 'agg_qty', 'chk_emp_id', 'chk_emp_num', 
            'svc_rnd_num', 'seat_num', 'menu_item'
        ]