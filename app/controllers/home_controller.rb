class HomeController < ApplicationController

	def index
		@url = "Hello there!"
		@show_all = Datum.all
	end

	def show
		@show = Datum.all.find_by(id: params[:id])
		puts params[:id]
	end
	
	def create
		url = params[:url]
		content = `python lib/assets/python/crawling_action.py "#{url}"`
		web = content.split("|")[1].split("\n")[0]
		begin
			Datum.create!(web: web, about: content.split("|")[0])
			puts "...Crawling #{url} Complete!!"
		rescue
			puts "...We have #{url} already!!"
		end
		
		redirect_to home_path(Datum.find_by(web: web))
	end

	def update
		id = params[:id]
		url = params[:url]
		content = `python lib/assets/python/crawling_action.py "#{url}"`
		Datum.find(id).update(about: content.split("|")[0])
		puts "...Crawling #{url} Complete!!"
		
		redirect_to home_index_path
	end

	def destroy
		id = params[:id]
		Datum.find(id).delete
		
		redirect_to home_index_path
	end



end
