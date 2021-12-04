class CreateData < ActiveRecord::Migration[6.1]
  def change
    create_table :data do |t|
	  t.string :web, index: {unique: true}
	  t.string :about
      t.timestamps
    end
  end
end
