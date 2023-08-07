from django.shortcuts import render
from rest_framework.views import Response,APIView
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from rest_framework import status
from .models import *
from rest_framework.decorators import action
# Create your views here.

class UserView(APIView):
    def post(self,request,*args,**kwargs):
        try:
            new_user=UserModelSerializers(data=request.data)
            if new_user.is_valid():
                new_user.save()
                return Response({"msg":"ok"})
            else:
                return Response({"msg":new_user.errors},status=status.HTTP_404_NOT_FOUND)
        except:
            return Response({"msg":"failed"},status=status.HTTP_404_NOT_FOUND)

class ProductView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializers
    model=Product

    @action(detail=False, methods=['GET'])
    def search(self,request):
            productname = request.query_params.get('productname', None)
            queryset = self.get_queryset()
            
            if productname:
                queryset = queryset.filter(productname__icontains=productname)
            
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
    @action(detail=True,methods=['GET'])
    def post(self, request):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    @action(detail=True,methods=['GET'])
    def post(self, request):
        cart = Cart.objects.get(user=request.user)
        product = Product.objects.get(pk=request.data.get('product_id'))
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(cart=cart, product=product)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True,methods=['get'])
    def get_review(self,request,*args,**kwargs):
        did=kwargs.get("pk")
        Product=Product.objects.get(id=did)
        qs=Reviews.objects.filter(product=Product)
        ser=ReviewSerializer(qs,many=True)
        return Response(data=ser.data)
    
    @action(detail=True,methods=['post'])
    def add_review(self,request,*args,**kwargs):
        did=kwargs.get("pk")
        product=Product.objects.get(id=did)
        user=request.user
        ser=ReviewSerializer(data=request.data,context={"user":user,"product":product})
        if ser.is_valid():
            ser.save()
            return Response(data=ser.data)
        else:
            return Response({"msg":"Failed"},status=status.HTTP_404_NOT_FOUND)
        

class CartView(APIView):
    def post(self, request):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CartItemView(APIView):
    def post(self, request):
        cart = Cart.objects.get(user=request.user)
        product = Product.objects.get(pk=request.data.get('product_id'))
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(cart=cart, product=product)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @action(detail=True,methods=['get'])
    def get_review(self,request,*args,**kwargs):
        did=kwargs.get("pk")
        Product=Product.objects.get(id=did)
        qs=Reviews.objects.filter(product=Product)
        ser=ReviewSerializer(qs,many=True)
        return Response(data=ser.data)
    

    @action(detail=True,methods=['post'])
    def add_review(self,request,*args,**kwargs):
        did=kwargs.get("pk")
        product=Product.objects.get(id=did)
        user=request.user
        ser=ReviewSerializer(data=request.data,context={"user":user,"product":product})
        if ser.is_valid():
            ser.save()
            return Response(data=ser.data)
        else:
            return Response({"msg":"Failed"},status=status.HTTP_404_NOT_FOUND)